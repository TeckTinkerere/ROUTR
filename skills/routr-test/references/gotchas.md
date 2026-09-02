# Test gotchas

1. **Pass-first TDD**: writing the implementation before the failing test defeats the point — the test never proves it would have caught the bug.
2. **Flaky retry loop**: adding `retries: 3` to a flaky E2E test hides a real race condition instead of fixing it.
3. **Implementation-detail assertions**: asserting on internal state/props instead of observable behavior breaks tests on every refactor even when behavior is unchanged.
4. **Wrong level**: writing an E2E test for pure logic that a unit test would cover in milliseconds.
5. **No run command documented**: a test suite nobody can invoke the same way twice isn't part of CI, it's a demo.
6. **routr-test vs routr-qa confusion**: "check the site works" is `routr-qa`, not a request to author new spec files — see [boundaries.md](./boundaries.md).
