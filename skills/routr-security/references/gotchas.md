# Security gotchas

1. **Label without exploit path**: "SQL injection risk" with no concrete input that triggers it isn't a finding — it's a guess. Show the request/input that exploits it.
2. **Full-repo scan for a small diff**: running `semgrep` over the whole repo when only three files changed drowns real findings in pre-existing noise.
3. **Confusing lint with security**: a style warning is not a security finding — don't pad severity counts.
4. **Skipping the data layer**: an auth-path review that never checks RLS/Firestore rules misses the most common real-world break.
5. **Fixing inline**: patching the vulnerability from within `routr-security` instead of handing off to `routr-ship` skips that skill's own verification step.
