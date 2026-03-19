# Code Review Checklist (5 Dimensions)

Tech Lead Reviewer uses this. PASS/FAIL per dimension.

## D1: Code Quality & Patterns
- [ ] No magic numbers
- [ ] No dead code or commented-out code
- [ ] No god objects (>300 lines or >10 methods)
- [ ] Naming follows coding-standards.md
- [ ] SOLID principles evident
- [ ] Error handling consistent
- [ ] No code duplication

## D2: Security Conformance
- [ ] All CRITICAL findings from security report resolved
- [ ] All HIGH findings resolved
- [ ] Security coverage was thorough

## D3: Test Coverage
- [ ] All test cases from test plan implemented
- [ ] Coverage meets threshold
- [ ] Tests verify behaviour, not just coverage
- [ ] No flaky patterns

## D4: Architecture Conformance
- [ ] Files per source-tree.md
- [ ] Tech stack per tech-stack.md
- [ ] APIs per api-contracts.md
- [ ] No unapproved dependencies
- [ ] No deviation without ADR

## D5: Performance & Scalability
- [ ] No N+1 queries
- [ ] Pagination on list endpoints
- [ ] Async where appropriate
- [ ] Indexes for new query patterns
- [ ] No unbounded loops
