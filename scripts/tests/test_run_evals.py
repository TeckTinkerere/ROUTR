"""Unit tests for scripts/run-evals.py host mode. Stdlib only; no network.

    python -m unittest discover -s scripts/tests -v
"""
import contextlib
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
FAKE = str(HERE / "fake_claude.py")

_spec = importlib.util.spec_from_file_location("run_evals", HERE.parent / "run-evals.py")
run_evals = importlib.util.module_from_spec(_spec)
sys.modules["run_evals"] = run_evals  # dataclasses needs the module registered
_spec.loader.exec_module(run_evals)

SITUATIONAL = {"routr-debug", "routr-ship", "routr-deploy", "routr-security"}


def ev(obj):
    return json.dumps(obj)


def init(skills):
    return ev({"type": "system", "subtype": "init", "skills": skills, "tools": ["Skill"], "model": "m"})


def skill_call(name, tid=None, key="skill"):
    block = {"type": "tool_use", "name": "Skill", "input": {key: name}}
    if tid:
        block["id"] = tid
    return ev({"type": "assistant", "message": {"role": "assistant", "content": [block]}})


def interpret(lines):
    return run_evals.interpret_host(run_evals.parse_host_stream(lines), SITUATIONAL)


class StreamParsing(unittest.TestCase):
    def test_init_not_first_and_counts(self):
        lines = [
            ev({"type": "system", "subtype": "hook_started"}),
            "not json at all",
            init(["update-config", "routr-debug", "routr-router", "simplify"]),
            skill_call("routr-debug"),
            ev({"type": "result", "is_error": False, "result": "x"}),
        ]
        p = run_evals.parse_host_stream(lines)
        self.assertTrue(p.saw_init)
        self.assertEqual((p.skills_seen, p.routr_seen), (4, 2))
        r = interpret(lines)
        self.assertEqual((r.router, r.chain, r.reason), ("routr-debug", ["routr-debug"], None))

    def test_namespaced_and_slash_names(self):
        r = interpret([init([]), skill_call("/routr:routr-debug"), skill_call("pkg:routr-ship", key="name"),
                       skill_call("routr-deploy extra args", key="command")])
        self.assertEqual(r.chain, ["routr-debug", "routr-ship", "routr-deploy"])

    def test_router_first_sets_via_router(self):
        r = interpret([init([]), skill_call("routr-router"), skill_call("routr-security"), skill_call("routr-ship")])
        self.assertTrue(r.via_router)
        self.assertEqual(r.router, "routr-security")
        self.assertEqual(r.chain, ["routr-security", "routr-ship"])
        self.assertEqual(r.routr_invoked[0], "routr-router")

    def test_router_not_first_is_not_via_router(self):
        r = interpret([init([]), skill_call("routr-debug"), skill_call("routr-router")])
        self.assertFalse(r.via_router)
        self.assertEqual(r.chain, ["routr-debug"])

    def test_no_skill(self):
        r = interpret([init(["routr-debug"]), ev({"type": "result", "is_error": False, "result": "hi"})])
        self.assertIsNone(r.router)
        self.assertIsNone(r.chain)
        self.assertEqual(r.reason, "no-skill")

    def test_other_skill_recorded(self):
        r = interpret([init([]), skill_call("frontend-design"), skill_call("frontend-design")])
        self.assertEqual(r.reason, "no-skill")
        self.assertEqual(r.other_skills, ["frontend-design"])

    def test_router_only_is_no_situational(self):
        r = interpret([init([]), skill_call("routr-router")])
        self.assertIsNone(r.router)
        self.assertEqual(r.reason, "no-situational")

    def test_duplicate_invocations_deduped_in_order(self):
        r = interpret([
            init([]),
            skill_call("routr-debug", tid="a"), skill_call("routr-debug", tid="a"),
            skill_call("routr-ship", tid="b"), skill_call("routr-debug", tid="c"),
        ])
        self.assertEqual(r.chain, ["routr-debug", "routr-ship"])

    def test_auth_failure_is_error(self):
        lines = [
            init([]),
            ev({"type": "assistant", "error": "authentication_failed", "message": {"content": []}}),
            ev({"type": "result", "is_error": True, "result": "Not logged in"}),
        ]
        r = interpret(lines)
        self.assertEqual(r.reason, "error")
        self.assertIn("authentication_failed", r.error)

    def test_error_after_skill_still_scores(self):
        r = interpret([init([]), skill_call("routr-debug"),
                       ev({"type": "result", "is_error": True, "result": "max turns"})])
        self.assertEqual(r.router, "routr-debug")
        self.assertIsNone(r.reason)


class HostRuns(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="routr-test-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def write_eval(self, prompts):
        p = self.tmp / "tiny.eval.json"
        p.write_text(json.dumps({"skill": "tiny", "prompts": prompts}), encoding="utf-8")
        return p

    def write_script(self, mapping):
        p = self.tmp / "script.json"
        p.write_text(json.dumps(mapping), encoding="utf-8")
        return p

    def run_main(self, argv, env=None):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.dict(os.environ, env or {}), mock.patch.object(sys, "argv", ["run-evals.py"] + argv), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = run_evals.main()
        return code, out.getvalue(), err.getvalue()

    def test_auth_failure_preflight_exits_2(self):
        ev_path = self.write_eval([{"prompt": "ALPHA", "expected_router": "routr-debug"}])
        code, out, err = self.run_main(
            ["--mode", "host", "--claude-bin", FAKE, "--file", str(ev_path)],
            env={"FAKE_CLAUDE_MODE": "auth"},
        )
        self.assertEqual(code, 2)
        self.assertIn("preflight failed", err)
        self.assertIn("authentication_failed", err)
        self.assertIn("sign in", err)
        self.assertNotIn("Overall accuracy", out)

    def test_missing_cli_exits_2(self):
        ev_path = self.write_eval([{"prompt": "ALPHA", "expected_router": "routr-debug"}])
        code, _out, err = self.run_main(
            ["--mode", "host", "--claude-bin", str(self.tmp / "nope.py"), "--file", str(ev_path)])
        self.assertEqual(code, 2)
        self.assertIn("preflight failed", err)

    def test_end_to_end_scoring(self):
        ev_path = self.write_eval([
            {"prompt": "ALPHA crash", "expected_router": "routr-debug",
             "expected_chain": ["routr-debug", "routr-ship"]},
            {"prompt": "BETA go live", "expected_router": "routr-deploy"},
            {"prompt": "GAMMA nothing", "expected_router": "routr-ship", "expected_chain": ["routr-ship"]},
            {"prompt": "DELTA bug", "expected_router": "routr-debug",
             "expected_chain": ["routr-debug", "routr-ship"], "acceptable_chains": [["routr-debug"]]},
            {"prompt": "EPSILON bug", "expected_router": "routr-debug", "must_not_load": ["routr-deploy"]},
            {"prompt": "ZETA skipped", "expected_behaviors": ["x"]},
        ])
        script = self.write_script({
            "ALPHA": ["routr-debug", "routr-ship"],
            "BETA": ["routr-router", "routr-deploy"],
            "DELTA": ["routr:routr-debug"],
            "EPSILON": ["routr-deploy", "frontend-design"],
        })
        json_out = self.tmp / "out.json"
        code, out, err = self.run_main(
            ["--mode", "host", "--claude-bin", FAKE, "--file", str(ev_path), "--json", str(json_out),
             "--concurrency", "2"],
            env={"FAKE_CLAUDE_SCRIPT": str(script), "FAKE_CLAUDE_HOOK": "1"},
        )
        self.assertEqual(code, 0, err)
        # hits: ALPHA, BETA, DELTA = 3 of 5 scorable
        self.assertIn("Overall accuracy: 3/5 (60.0%)", out)
        # chain: ALPHA exact, GAMMA miss (no skill), DELTA exact via acceptable_chains
        self.assertIn("Chain exact-match:  2/3", out)
        self.assertIn("Chain prefix-match: 2/3", out)
        self.assertIn("must_not_load violations: 1", out)
        self.assertIn("Prompts skipped (no expected_router): 1", out)
        self.assertIn("No ROUTR skill invoked: 1/5 (20.0%)", out)
        self.assertIn("Routed via routr-router: 1/5 (20.0%)", out)
        self.assertIn("frontend-design x1", out)
        self.assertIn("[no-skill]", out)
        self.assertIn("Skills visible to the agent: min", out)

        data = json.loads(json_out.read_text(encoding="utf-8"))
        self.assertEqual(data["mode"], "host")
        self.assertEqual(data["chain_exact"], 2)
        self.assertEqual(data["host"]["via_router"], 1)
        by_prompt = {r["prompt"]: r for r in data["results"]}
        self.assertEqual(by_prompt["BETA go live"]["host"]["via_router"], True)
        self.assertEqual(by_prompt["GAMMA nothing"]["host"]["reason"], "no-skill")
        self.assertEqual(by_prompt["ALPHA crash"]["predicted_chain"], ["routr-debug", "routr-ship"])

    def test_min_accuracy_gate(self):
        ev_path = self.write_eval([{"prompt": "GAMMA nothing", "expected_router": "routr-ship"}])
        code, out, _err = self.run_main(
            ["--mode", "host", "--claude-bin", FAKE, "--file", str(ev_path), "--min-accuracy", "0.5"])
        self.assertEqual(code, 1)
        self.assertIn("FAIL: accuracy", out)

    def test_sandbox_contents_flags_and_cleanup(self):
        ev_path = self.write_eval([{"prompt": "ALPHA crash", "expected_router": "routr-debug"}])
        script = self.write_script({"ALPHA": ["routr-debug"]})
        noise = self.tmp / "noise"
        for name in ("alpha-skill", "beta-skill", "routr-fake"):
            (noise / name).mkdir(parents=True)
            (noise / name / "SKILL.md").write_text("---\nname: x\ndescription: d\n---\n", encoding="utf-8")
        log = self.tmp / "args.jsonl"
        code, out, err = self.run_main(
            ["--mode", "host", "--claude-bin", FAKE, "--file", str(ev_path), "--noise-dir", str(noise),
             "--host-env", "user", "--max-turns", "5", "--model", "fake-m"],
            env={"FAKE_CLAUDE_SCRIPT": str(script), "FAKE_CLAUDE_ARGS_LOG": str(log),
                 "FAKE_CLAUDE_USER_SKILLS": "u1,u2,u3"},
        )
        self.assertEqual(code, 0, err)
        self.assertIn("noise skills=2", out)
        calls = [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(calls), 2)  # preflight + one prompt
        argv = calls[-1]["argv"]
        for flag, val in [("--output-format", "stream-json"), ("--tools", "Skill"),
                          ("--permission-mode", "default"), ("--setting-sources", "user,project"),
                          ("--max-turns", "5"), ("--model", "fake-m"),
                          ("--settings", '{"disableAllHooks": true}')]:
            self.assertEqual(argv[argv.index(flag) + 1], val)
        for flag in ("-p", "--verbose", "--no-session-persistence"):
            self.assertIn(flag, argv)
        sandbox = Path(calls[-1]["cwd"])
        self.assertFalse(sandbox.exists(), "sandbox should be removed")
        # skills visible: routr-* folders + 2 noise + 2 bundled + 3 user
        n_routr = len(list(run_evals.SKILLS_DIR.glob("routr-*")))
        data_max = n_routr + 2 + 2 + 3
        self.assertIn(f"min {data_max}, max {data_max}", out)

    def test_keep_sandbox_and_isolated_default(self):
        ev_path = self.write_eval([{"prompt": "ALPHA crash", "expected_router": "routr-debug"}])
        log = self.tmp / "args.jsonl"
        code, _out, err = self.run_main(
            ["--mode", "host", "--claude-bin", FAKE, "--file", str(ev_path), "--keep-sandbox"],
            env={"FAKE_CLAUDE_ARGS_LOG": str(log)},
        )
        self.assertEqual(code, 0, err)
        call = json.loads(log.read_text(encoding="utf-8").splitlines()[-1])
        self.assertEqual(call["argv"][call["argv"].index("--setting-sources") + 1], "project")
        sandbox = Path(call["cwd"])
        try:
            self.assertTrue((sandbox / ".claude" / "skills" / "routr-debug" / "SKILL.md").exists())
        finally:
            shutil.rmtree(sandbox, ignore_errors=True)

    def test_bad_noise_dir_exits_2(self):
        ev_path = self.write_eval([{"prompt": "ALPHA", "expected_router": "routr-debug"}])
        code, _out, err = self.run_main(
            ["--mode", "host", "--claude-bin", FAKE, "--file", str(ev_path), "--noise-dir", str(self.tmp / "no")])
        self.assertEqual(code, 2)
        self.assertIn("--noise-dir", err)


class ChainScores(unittest.TestCase):
    def test_acceptable_chains(self):
        exp = ["routr-debug", "routr-ship"]
        self.assertEqual(run_evals.chain_scores(exp, ["routr-debug", "routr-ship"]), (True, True))
        self.assertEqual(run_evals.chain_scores(exp, ["routr-debug"]), (False, False))
        self.assertEqual(run_evals.chain_scores(exp, ["routr-debug"], [["routr-debug"]]), (True, True))
        self.assertEqual(run_evals.chain_scores(exp, None, [["routr-debug"]]), (False, False))


class Helpers(unittest.TestCase):
    def test_py_bin_runs_under_this_python(self):
        self.assertEqual(run_evals.claude_command("x/fake.py"), [sys.executable, "x/fake.py"])
        self.assertEqual(run_evals.claude_command("claude.exe"), ["claude.exe"])


if __name__ == "__main__":
    unittest.main()
