# Graph Report - ROUTR  (2026-10-09)

## Corpus Check
- 134 files · ~52,693 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1085 nodes · 1469 edges · 70 communities (67 shown, 3 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `aa01be53`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- routr-agents
- routr-review
- routr-frontend
- routr-mobile
- routr-video
- routr-test
- ROUTR README
- routr-plan
- Rename map (v2)
- install-routr.sh script
- routr-perf
- QA examples
- run-evals.py
- Debug workflow
- routr-debug
- Skill registry — dependencies for routr-* routers
- Ship workflow
- Changelog
- routr-explore
- routr-frontend/SKILL.md
- Security examples
- routr-security
- routr-motion
- routr-qa
- routr-ship
- routr-deploy
- routr-plan/SKILL.md
- routr-integrate
- routr-ai
- routr-database
- README.md
- Install — ROUTR v2
- Audit process (complete each phase before the next)
- skill-registry.md
- Architecture
- Video examples
- Contributor Covenant Code of Conduct
- Design
- routr-depth-frontend
- routr-router
- routr-depth-debug
- routr-depth-test
- Plan
- routr-depth-ship
- Overlap resolution
- Video Remotion workflow
- Contributing to ROUTR
- Skill resolution (all routr-* routers)
- HyperFrames stack configuration
- Audio, media, and HeyGen configuration
- Data-driven video
- Product marketing video
- Authoring ROUTR skills
- How ROUTR routes
- Video generation skills — ROUTR leaderboard
- sync-installed.sh
- routr-video boundaries
- Video gotchas
- Video launch workflow
- routr-catalog
- PULL_REQUEST_TEMPLATE.md
- Stacks
- validate-skills.sh
- Security Policy
- Video fallback (no child skills installed)
- Multi-route plans
- routr-motion/references/boundaries.md

## God Nodes (most connected - your core abstractions)
1. `routr-frontend` - 62 edges
2. `routr-debug` - 51 edges
3. `routr-ship` - 50 edges
4. `routr-plan` - 44 edges
5. `routr-video` - 42 edges
6. `routr-agents` - 41 edges
7. `routr-motion` - 40 edges
8. `routr-test` - 39 edges
9. `routr-mobile` - 36 edges
10. `routr-router` - 36 edges

## Surprising Connections (you probably didn't know these)
- `agent-design-playbook` --conceptually_related_to--> `routr-agents`  [EXTRACTED]
  docs/naming.md → skills/routr-agents/SKILL.md
- `debugging-playbook` --conceptually_related_to--> `routr-debug`  [EXTRACTED]
  docs/naming.md → skills/routr-debug/SKILL.md
- `deploy-playbook` --conceptually_related_to--> `routr-deploy`  [EXTRACTED]
  docs/naming.md → skills/routr-deploy/SKILL.md
- `frontend-feature-playbook` --conceptually_related_to--> `routr-frontend`  [EXTRACTED]
  docs/naming.md → skills/routr-frontend/SKILL.md
- `library-integration-playbook` --conceptually_related_to--> `routr-integrate`  [EXTRACTED]
  docs/naming.md → skills/routr-integrate/SKILL.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **routr-depth-* fallback skills** — skills_routr_depth_debug_skill_routr_depth_debug, skills_routr_depth_frontend_skill_routr_depth_frontend, skills_routr_depth_plan_skill_routr_depth_plan, skills_routr_depth_ship_skill_routr_depth_ship, skills_routr_depth_test_skill_routr_depth_test [EXTRACTED 0.90]
- **routr-debug reference documentation set** — skills_routr_debug_skill_routr_debug, skills_routr_debug_references_workflow_workflow, skills_routr_debug_references_fallback_fallback, skills_routr_debug_references_gotchas_gotchas, skills_routr_debug_references_examples_examples, skills_routr_debug_references_boundaries_boundaries [EXTRACTED 0.95]
- **ROUTR situational routers (top layer)** — skills_routr_debug_skill_routr_debug, skills_routr_ship_skill_routr_ship, skills_routr_frontend_skill_routr_frontend, skills_routr_plan_skill_routr_plan, skills_routr_test_skill_routr_test, skills_routr_review_skill_routr_review, skills_routr_refactor_skill_routr_refactor, skills_routr_deploy_skill_routr_deploy, skills_routr_database_skill_routr_database, skills_routr_qa_skill_routr_qa, skills_routr_security_skill_routr_security, skills_routr_explore_skill_routr_explore, skills_routr_integrate_skill_routr_integrate, skills_routr_agents_skill_routr_agents, skills_routr_motion_skill_routr_motion, skills_routr_mobile_skill_routr_mobile, skills_routr_marketing_skill_routr_marketing, skills_routr_ai_skill_routr_ai, skills_routr_video_skill_routr_video [EXTRACTED 0.95]
- **ROUTR Depth Fallback Skills** — skills_routr_depth_debug_skill_routr_depth_debug, skills_routr_depth_frontend_skill_routr_depth_frontend, skills_routr_depth_plan_skill_routr_depth_plan, skills_routr_depth_ship_skill_routr_depth_ship, skills_routr_depth_test_skill_routr_depth_test [EXTRACTED 1.00]
- **routr-frontend Skill + Reference Docs** — skills_routr_frontend_skill_routr_frontend, skills_routr_frontend_references_boundaries_boundaries, skills_routr_frontend_references_examples_examples, skills_routr_frontend_references_fallback_fallback, skills_routr_frontend_references_gotchas_gotchas, skills_routr_frontend_references_workflow_workflow [EXTRACTED 1.00]
- **routr-plan Skill + Reference Docs** — skills_routr_plan_skill_routr_plan, skills_routr_plan_references_boundaries_boundaries, skills_routr_plan_references_examples_examples, skills_routr_plan_references_fallback_fallback, skills_routr_plan_references_gotchas_gotchas, skills_routr_plan_references_workflow_workflow [EXTRACTED 1.00]
- **routr-ship Reference Documentation Bundle** — skills_routr_ship_skill_routr_ship, skills_routr_ship_references_workflow_workflow, skills_routr_ship_references_fallback_fallback, skills_routr_ship_references_gotchas_gotchas, skills_routr_ship_references_examples_examples, skills_routr_ship_references_boundaries_boundaries [EXTRACTED 1.00]
- **routr-video Reference Documentation Bundle** — skills_routr_video_skill_routr_video, skills_routr_video_references_launch_launch, skills_routr_video_references_remotion_remotion, skills_routr_video_references_gotchas_gotchas, skills_routr_video_references_examples_examples, skills_routr_video_references_boundaries_boundaries [EXTRACTED 1.00]
- **ROUTR Router Skill System** — skills_routr_router_skill_routr_router, skills_routr_qa_skill_routr_qa, skills_routr_refactor_skill_routr_refactor, skills_routr_review_skill_routr_review, skills_routr_security_skill_routr_security, skills_routr_ship_skill_routr_ship, skills_routr_test_skill_routr_test, skills_routr_video_skill_routr_video [INFERRED 0.85]

## Communities (70 total, 3 thin omitted)

### Community 0 - "routr-agents"
Cohesion: 0.06
Nodes (30): routr-agents boundaries, routr-agents vs routr-ai, 0. Bootstrap, 1. Clarify, 2. Design, 3. Implement, Companion checklist, Do not activate (+22 more)

### Community 1 - "routr-review"
Cohesion: 0.05
Nodes (43): caveman-review, improve-codebase-architecture, receiving-code-review, review-animations, caveman-review, code-review-excellence, improve-codebase-architecture, receiving-code-review (+35 more)

### Community 2 - "routr-frontend"
Cohesion: 0.09
Nodes (22): tailwind-design-system, ui-ux-pro-max, vercel-react-best-practices, web-design-guidelines, shadcn, tailwind-design-system, ui-ux-pro-max, routr-frontend Gotchas (+14 more)

### Community 3 - "routr-mobile"
Cohesion: 0.05
Nodes (41): ai-seo, aso, building-native-ui, copywriting, expo-deployment, native-data-fetching, seo-audit, vercel-react-native-skills (+33 more)

### Community 4 - "routr-video"
Cohesion: 0.09
Nodes (38): video-launch-playbook, brag, embedded-captions, faceless-explainer, find-docs, hyperframes, motion-graphics, pr-to-video (+30 more)

### Community 5 - "routr-test"
Cohesion: 0.11
Nodes (19): playwright-best-practices, playwright-cli, tdd, test-driven-development, 0. Bootstrap, 1. Choose test level (medium freedom), 2. TDD loop (low freedom), 3. Verify (low freedom) (+11 more)

### Community 6 - "ROUTR README"
Cohesion: 0.57
Nodes (7): Authoring ROUTR Skills, ROUTR Naming Taxonomy, ROUTR Discussions Welcome Template, ROUTR Install Guide, ROUTR README, Skill Catalog (deprecated), ROUTR Skill Registry

### Community 7 - "routr-plan"
Cohesion: 0.07
Nodes (36): brainstorming (Obra), executing-plans (Obra), find-skills, grill-me, grill-with-docs, improve-codebase-architecture, to-prd, brainstorming (+28 more)

### Community 8 - "Rename map (v2)"
Cohesion: 0.09
Nodes (23): Adding a new router, agent-design-playbook, Child skills (external), code-review-playbook, debugging-playbook, deploy-playbook, Description format, e2e-qa-playbook (+15 more)

### Community 11 - "routr-perf"
Cohesion: 0.04
Nodes (40): routr-perf boundaries, vs routr-database, vs routr-debug, vs routr-motion, vs routr-refactor, Example 1: Slow dashboard load, Example 2: Bundle size complaint, Example 3: Component re-renders too often (+32 more)

### Community 12 - "QA examples"
Cohesion: 0.06
Nodes (26): routr-qa boundaries, routr-qa vs routr-test, Example 1: Post-deploy smoke test, Example 2: "Write a test for the login flow", Example 3: Exploratory bug hunt, Example 4: No preview exists, QA examples, Escalate to install (+18 more)

### Community 13 - "run-evals.py"
Cohesion: 0.12
Nodes (32): Path, ask_claude(), build_menu(), chain_scores(), load_candidate_routers(), load_handoffs(), load_route_hints(), load_router() (+24 more)

### Community 14 - "Debug workflow"
Cohesion: 0.08
Nodes (20): Precedence (more specific wins), routr-debug boundaries, vs routr-ship, vs routr-test, Debug examples, Example 1: TypeError on click, Example 2: Test fails only in CI, Example 3: User wants commit immediately (+12 more)

### Community 15 - "routr-debug"
Cohesion: 0.10
Nodes (25): Skill Resolution (routr-catalog), caveman, context-degradation, diagnosing-bugs, lean-ctx, symdex-code-search, systematic-debugging, routr-debug Examples (+17 more)

### Community 16 - "Skill registry — dependencies for routr-* routers"
Cohesion: 0.08
Nodes (25): Agent & loop engineering, AI / LLM, Code intelligence & context, Code review, Context engineering, Database, Debugging & quality, Deploy (+17 more)

### Community 17 - "Ship workflow"
Cohesion: 0.09
Nodes (16): routr-ship boundaries, Example 1: Typo fix, Example 2: Bug already diagnosed, Example 3: Huge diff, Ship examples, Commit format, PR minimum, Ship fallback (+8 more)

### Community 18 - "Changelog"
Cohesion: 0.10
Nodes (20): [1.0.0] - 2026-07-01, [1.1.0] - 2026-07-01, [1.2.0] - 2026-07-01, [1.3.0] - 2026-07-01, [2.0.0] - 2026-07-03, [2.0.1] - 2026-09-05, [2.1.0] - Unreleased, Added (+12 more)

### Community 19 - "routr-explore"
Cohesion: 0.10
Nodes (19): explore-codebase-playbook, context-fundamentals, lean-ctx, symdex-code-search, routr-explore boundaries, 0. Bootstrap, 1. Frame question, 2. Map (SymDex) (+11 more)

### Community 20 - "routr-frontend/SKILL.md"
Cohesion: 0.10
Nodes (15): routr-frontend boundaries, vs routr-motion, Example 1: SaaS landing, Example 2: Dashboard, Example 3: "Make it pop", Frontend examples, Frontend fallback (no frontend-design installed), Install full skill (+7 more)

### Community 21 - "Security examples"
Cohesion: 0.10
Nodes (14): routr-review boundaries, routr-security boundaries, routr-security vs routr-review, Example 1: Pre-launch audit, Example 2: Scoped PR check, Example 3: RLS policy review, Example 4: Non-security bug (boundary case), Security examples (+6 more)

### Community 22 - "routr-security"
Cohesion: 0.10
Nodes (20): security-review-playbook, firebase-security-rules-auditor, firebase-security-rules-auditor, semgrep, routr-debug Boundaries, 0. Bootstrap, 1. Scope (low freedom), 2. Static analysis (medium freedom) (+12 more)

### Community 23 - "routr-motion"
Cohesion: 0.10
Nodes (20): motion-design, review-animations, ui-animation, framer-motion-animator, motion-design, ui-animation, routr-frontend Examples, 0. Bootstrap (+12 more)

### Community 24 - "routr-qa"
Cohesion: 0.10
Nodes (20): agent-browser, agent-browser, playwright-best-practices, playwright-cli, 0. Bootstrap, 1. Mode (medium freedom), 2. Exploratory (medium freedom), 3. Automated E2E (medium freedom) (+12 more)

### Community 25 - "routr-ship"
Cohesion: 0.11
Nodes (20): caveman-commit, finishing-a-development-branch, lean-ctx, requesting-code-review, caveman-commit, routr-ship Examples, routr-ship Fallback, routr-ship Gotchas (+12 more)

### Community 26 - "routr-deploy"
Cohesion: 0.10
Nodes (18): deploy-to-vercel, finishing-a-development-branch, vercel-cli-with-tokens, vercel-optimize, routr-deploy boundaries, 0. Bootstrap, 1. Pre-deploy gate, 2. Deploy (+10 more)

### Community 27 - "routr-plan/SKILL.md"
Cohesion: 0.10
Nodes (14): routr-plan boundaries, Example 1: "Add auth", Example 2: "Grill my startup idea", Example 3: Small bugfix, Planning examples, Minimum brainstorm, Minimum PRD gate, Planning fallback (+6 more)

### Community 28 - "routr-integrate"
Cohesion: 0.11
Nodes (17): find-docs, framer-motion-animator, shadcn, routr-frontend Boundaries Table, routr-integrate boundaries, 0. Bootstrap, 1. Verify docs, 2. Repo alignment (+9 more)

### Community 29 - "routr-ai"
Cohesion: 0.11
Nodes (18): ai-llm-app-playbook, docs/naming.md (deprecated skill names), 0. Bootstrap, 1. Patterns, 2. Safety, Anti-patterns, Do not activate, Handoff (+10 more)

### Community 30 - "routr-database"
Cohesion: 0.11
Nodes (16): database-playbook, supabase, supabase-postgres-best-practices, routr-database boundaries, 0. Bootstrap, 1. Discover, 2. Schema & migrations, 3. Query work (+8 more)

### Community 31 - "README.md"
Cohesion: 0.14
Nodes (11): All routers, Child bundles, Contributing and community, Example flows, How routing works, License, Measured routing quality, Quality & upkeep (+3 more)

### Community 32 - "Install — ROUTR v2"
Cohesion: 0.14
Nodes (14): Bundle picker, Install all routr-* skills (no prompts), Install child skill bundles (required for depth), Install routers, Install — ROUTR v2, Interactive (recommended), Keep installed copies in sync, Per-agent paths (+6 more)

### Community 33 - "Audit process (complete each phase before the next)"
Cohesion: 0.14
Nodes (13): Audit process (complete each phase before the next), Install full skills, Iron law, Phase 1: Scope and threat model, Phase 2: AuthN / AuthZ and IDOR, Phase 3: Injection (SQL / NoSQL / command / XSS), Phase 4: Secrets in code and env, Phase 5: Supabase RLS / Firebase rules (+5 more)

### Community 35 - "Architecture"
Cohesion: 0.15
Nodes (13): Architecture, Authoring new routers, Compatibility, Discovery noise problem, Frontend stack, Layers, Multi-route planning, Naming (+5 more)

### Community 36 - "Video examples"
Cohesion: 0.15
Nodes (12): 10. Boundary — in-app motion, 11. Boundary — screen recording, 1. Brag, 2. Per-record variants, 3. Product promo from a URL, 4. Site tour, 5. Script with no site, 6. Metrics recap (+4 more)

### Community 37 - "Contributor Covenant Code of Conduct"
Cohesion: 0.17
Nodes (12): 1. Correction, 2. Warning, 3. Temporary Ban, 4. Permanent Ban, Attribution, Contributor Covenant Code of Conduct, Enforcement, Enforcement Guidelines (+4 more)

### Community 38 - "Design"
Cohesion: 0.17
Nodes (12): 1. Route plans: one router active, the whole route announced upfront, 2. Companions: a second router's checklist, not a second owner, 3. `routes.json`: the machine-readable source of truth, 4. Tie-break: the domain's own machinery beats generic debug, 5. Evals understand chains and alternatives, 6. Open-source readiness, Design, Next (+4 more)

### Community 39 - "routr-depth-frontend"
Cohesion: 0.17
Nodes (11): frontend-design (Anthropic Skill), frontend-design, Avoid default AI clusters (unless brief requires), Build rules, CSS discipline, Design plan (required before code), Ground in the subject, Install full skill (+3 more)

### Community 40 - "routr-router"
Cohesion: 0.18
Nodes (11): playbook-router, routr-catalog resolution.md (router precedence), After routing, Companions, Decision tree, Do not activate, Frontend detection, Iron law (+3 more)

### Community 41 - "routr-depth-debug"
Cohesion: 0.18
Nodes (10): systematic-debugging (Obra), Four phases (complete each before next), Install full skill, Iron law, Phase 1: Root cause investigation, Phase 2: Hypothesis, Phase 3: Fix, Phase 4: Verify (+2 more)

### Community 42 - "routr-depth-test"
Cohesion: 0.18
Nodes (10): test-driven-development (Obra), webapp-testing (Anthropic Skill), webapp-testing, Choose level, E2E discipline, Install full skills, Iron law, routr-depth-test (+2 more)

### Community 43 - "Plan"
Cohesion: 0.20
Nodes (10): Analysis — where ROUTR stands, Follow-ups (done), Open, Plan, Results (2026-09-25), ROUTR v2.1 — improvement plan (2026-09-25), Track A — tooling (scripts/, .github/), Track B — content (skills/, docs/, README, INSTALL, .plugin) (+2 more)

### Community 44 - "routr-depth-ship"
Cohesion: 0.20
Nodes (9): caveman-commit, requesting-code-review (Obra), Commit format, Install full skill, Iron law, PR minimum, routr-depth-ship, Scope (+1 more)

### Community 45 - "Overlap resolution"
Cohesion: 0.20
Nodes (10): AI feature, Deprecated names, Domain machinery vs generic debug, Extended decision tree, "Fix the UI" — bug or design?, Multi-intent requests, Overlap resolution, "Ship the feature" (+2 more)

### Community 46 - "Video Remotion workflow"
Cohesion: 0.20
Nodes (10): Bootstrap, Build pass, Composition configuration, New project, Non-negotiables, Port to HyperFrames, Rule index — load only what the task needs, Ship (+2 more)

### Community 47 - "Contributing to ROUTR"
Cohesion: 0.22
Nodes (9): Add a router, Commit style, Contributing to ROUTR, Improve a description, Local setup, Pick your path, Pull request checklist, Releases (maintainers) (+1 more)

### Community 48 - "Skill resolution (all routr-* routers)"
Cohesion: 0.22
Nodes (9): How to load a child skill, If a child skill is missing, Multi-router requests, Removed playbook names, Router precedence, Skill resolution (all routr-* routers), Skills root, Stack entry points vs workflow selectors (+1 more)

### Community 50 - "HyperFrames stack configuration"
Cohesion: 0.22
Nodes (9): CLI dev loop, Cloud rendering, Completion gate, Configuration flags worth knowing, Creative direction, HyperFrames stack configuration, Layer map — load on demand, never all at once, Registry blocks and components (+1 more)

### Community 51 - "Audio, media, and HeyGen configuration"
Cohesion: 0.22
Nodes (9): Audio, media, and HeyGen configuration, Avatar / talking-head presenters, Captions, Cost rule, Preflight — mandatory before generating any audio, Resolving media assets, The audio engine — one entry point, The one switch: is there a HeyGen credential? (+1 more)

### Community 52 - "Data-driven video"
Cohesion: 0.25
Nodes (8): Data-driven video, Data prep — before any composition work, Handoff, Iron law, Motion rules for numbers, Per-record renders — the Remotion path, Single data video — the HyperFrames path, Verify

### Community 53 - "Product marketing video"
Cohesion: 0.25
Nodes (8): Beat structure, Channel spec, Handoff, Input modes, Iron law, Product marketing video, Publishing, Truth gate (low freedom)

### Community 54 - "Authoring ROUTR skills"
Cohesion: 0.29
Nodes (7): Authoring ROUTR skills, Checklist before PR, Child skill references, Folder layout, Freedom levels, SKILL.md template, Skill types

### Community 55 - "How ROUTR routes"
Cohesion: 0.29
Nodes (7): Companions, How ROUTR routes, Route plans, Single route, Tie-breaks, Where this is defined, Worked examples

### Community 56 - "Video generation skills — ROUTR leaderboard"
Cohesion: 0.29
Nodes (7): Honorable mentions, Install bundles, Sources, Stack decision (30 seconds), Top 10, Video generation skills — ROUTR leaderboard, Why brag ranks #2 overall but #1 for launch

### Community 57 - "sync-installed.sh"
Cohesion: 0.40
Nodes (5): is_legacy_name(), LEGACY_NAMES, REPO_SKILLS, ROOTS, sync-installed.sh script

### Community 58 - "routr-video boundaries"
Cohesion: 0.33
Nodes (5): Actions that need the user, not the agent, Internal splits, Precedence over self-declared entry points, routr-video boundaries, Workflows vs capability layers

### Community 59 - "Video gotchas"
Cohesion: 0.33
Nodes (6): Audio and media, Content, Deadline, Pipeline, Routing, Video gotchas

### Community 60 - "Video launch workflow"
Cohesion: 0.33
Nodes (6): Bootstrap, brag pass, HyperFrames pass, Route tree, Share and ship, Video launch workflow

### Community 61 - "routr-catalog"
Cohesion: 0.40
Nodes (5): Two-layer model, playbook-common, Child skill loading, Files, routr-catalog

### Community 62 - "PULL_REQUEST_TEMPLATE.md"
Cohesion: 0.40
Nodes (4): Checklist, Eval results, Type, What and why

### Community 63 - "Stacks"
Cohesion: 0.40
Nodes (5): AI / LLM apps, Marketing & SEO, Mobile · Expo / React Native, Stacks, Video · brag, HyperFrames, Remotion

### Community 64 - "validate-skills.sh"
Cohesion: 0.60
Nodes (3): emit_section(), note_fail(), validate-skills.sh script

### Community 65 - "Security Policy"
Cohesion: 0.40
Nodes (5): Reporting, Security Policy, Staying safe as a user, Supported versions, What counts as a vulnerability

### Community 66 - "Video fallback (no child skills installed)"
Cohesion: 0.40
Nodes (5): Escalate to install, Iron law, Minimum process, Video fallback (no child skills installed), When stuck

### Community 67 - "Multi-route plans"
Cohesion: 0.50
Nodes (4): Chain evals, Companions, Multi-route plans, Tie-break: the domain beats generic debug

## Ambiguous Edges - Review These
- `routr-explore` → `lean-ctx`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md · relation: references
- `routr-frontend` → `lean-ctx`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md · relation: references
- `routr-refactor` → `lean-ctx`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md · relation: references
- `routr-ship` → `lean-ctx`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md · relation: references

## Knowledge Gaps
- **722 isolated node(s):** `install-routr.sh script`, `ROOTS`, `LEGACY_NAMES`, `REPO_SKILLS`, `What and why` (+717 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `routr-explore` and `lean-ctx`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `routr-frontend` and `lean-ctx`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `routr-refactor` and `lean-ctx`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `routr-ship` and `lean-ctx`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ROUTR README` connect `ROUTR README` to `routr-agents`, `routr-review`, `routr-frontend`, `routr-mobile`, `routr-video`, `routr-test`, `routr-plan`, `routr-debug`, `routr-explore`, `routr-security`, `routr-motion`, `routr-qa`, `routr-ship`, `routr-deploy`, `routr-integrate`, `routr-ai`, `routr-database`, `Architecture`, `routr-depth-frontend`, `routr-router`, `routr-depth-debug`, `routr-depth-test`, `routr-depth-ship`, `routr-catalog`?**
  _High betweenness centrality (0.176) - this node is a cross-community bridge._
- **Why does `Architecture` connect `Architecture` to `skill-registry.md`, `routr-catalog`, `ROUTR README`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Why does `routr-video` connect `routr-video` to `routr-frontend`, `routr-mobile`, `ROUTR README`, `Rename map (v2)`, `routr-router`, `routr-debug`, `routr-video/SKILL.md`, `routr-motion`, `routr-ship`, `routr-deploy`, `routr-ai`?**
  _High betweenness centrality (0.151) - this node is a cross-community bridge._