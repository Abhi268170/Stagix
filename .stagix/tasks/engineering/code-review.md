# Task: code-review

## Purpose

Tech Lead Reviewer's 5-dimension review protocol. Every dimension produces a PASS or FAIL. All 5 must PASS for the story to proceed.

## Pre-Review Inputs

Before starting, read:
1. The story (from Engineering Lead context)
2. `.stagix/docs/architecture/coding-standards.md`
3. `.stagix/docs/architecture/tech-stack.md`
4. `.stagix/docs/architecture/source-tree.md`
5. `.stagix/docs/security-report-{story-key}.md` (Security Specialist's findings)
6. `.stagix/tests/{story-key}-test-plan.md` (Test Specialist's cases)
7. `.stagix/core-config.yaml` → `quality.coverage_threshold`

## Dimension 1: Code Quality & Patterns

**Check:**
- [ ] No magic numbers (constants defined)
- [ ] No dead code or commented-out code
- [ ] No god objects (>300 lines or >10 methods)
- [ ] Naming follows coding-standards.md conventions
- [ ] Appropriate abstraction level (not over or under-engineered)
- [ ] SOLID principles evident
- [ ] Error handling consistent with project patterns
- [ ] No code duplication (DRY)

**FAIL criteria**: Any shortcut, anti-pattern, or coding standard violation found.

## Dimension 2: Security Conformance

**Check:**
- [ ] Read security-report-{story-key}.md
- [ ] ALL CRITICAL findings resolved (grep for the fix)
- [ ] ALL HIGH findings resolved
- [ ] Security Specialist's coverage was thorough (no obvious gaps)
- [ ] Any new security concerns beyond what Specialist found

**FAIL criteria**: Any unresolved CRITICAL/HIGH finding.

## Dimension 3: Test Coverage

**Check:**
- [ ] Every test case in test-plan.md is implemented
- [ ] Tests actually test behaviour (not just coverage padding)
- [ ] No flaky patterns (hard waits, order-dependent tests)
- [ ] Edge cases from story are tested
- [ ] Run coverage check: meets threshold from core-config.yaml

**FAIL criteria**: Coverage below threshold OR test cases missing.

## Dimension 4: Architecture Conformance

**Check:**
- [ ] Files placed per source-tree.md
- [ ] Technologies match tech-stack.md (exact versions)
- [ ] API implementations match api-contracts.md
- [ ] No unapproved dependencies introduced
- [ ] Design patterns match architecture.md
- [ ] No deviation without an approved ADR

**FAIL criteria**: Any deviation from approved architecture.

## Dimension 5: Performance & Scalability

**Check:**
- [ ] No N+1 query patterns (check ORM eager loading)
- [ ] Pagination on list endpoints
- [ ] Async where appropriate (I/O bound operations)
- [ ] Database indexes exist for new query patterns
- [ ] No unbounded loops or memory accumulation
- [ ] Cache opportunities considered

**FAIL criteria**: Obvious performance issue in a critical path.

## Output

Write review to `.stagix/docs/code-review-{story-key}.md` per the agent's output format. Include PASS/FAIL per dimension with specific findings.
