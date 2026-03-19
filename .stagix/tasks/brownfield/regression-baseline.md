# Task: regression-baseline

## Purpose

Capture the existing test suite pass rate before any engineering work begins on an epic. This baseline is used to ensure that no story reduces the existing test pass rate.

## When to Run

Before the first story of each epic in brownfield mode. Run by the DevOps agent as step 0 of the engineering sequence.

## Protocol

### Step 1: Identify Test Command
Read `.stagix/core-config.yaml` → `quality.linters` and detected test framework to determine the correct test command:
- Python/pytest: `python -m pytest --tb=short -q`
- Node/jest: `npx jest --ci`
- Node/vitest: `npx vitest run`
- Go: `go test ./...`
- Ruby/rspec: `bundle exec rspec`

### Step 2: Run Test Suite
Execute the test command and capture:
- Total tests
- Passed tests
- Failed tests
- Skipped tests
- Pass rate percentage

### Step 3: Save Baseline
Write results to `.stagix/baselines/{epic-key}.json`:
```json
{
  "epic_key": "PROJ-E1",
  "captured_at": "2026-03-18T10:00:00Z",
  "test_command": "python -m pytest --tb=short -q",
  "total": 142,
  "passed": 138,
  "failed": 4,
  "skipped": 0,
  "pass_rate": 97.2,
  "known_failures": [
    "test_legacy_export.py::test_csv_encoding — known flaky, tracked in PROJ-99"
  ]
}
```

### Step 4: Set Regression Threshold
Write the pass rate to `core-config.yaml` → `brownfield.regression_threshold`.
The threshold is: `current_pass_rate` (pass rate cannot drop).

## Enforcement

After every story implementation:
1. The `block-git-commit.py` hook runs the test suite
2. Compares pass rate against baseline
3. If pass rate drops below baseline: commit blocked
4. Specific newly-failing tests listed in the error message
5. Developer must fix regressions before committing
