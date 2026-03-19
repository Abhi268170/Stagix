# SPRINT-008: Phase 9+10 — Integration & Brownfield Testing

**Status**: STRUCTURAL VALIDATION DONE — Live pipeline test requires Jira/Confluence credentials
**Priority**: P0 — Validates the entire system works end-to-end
**Estimate**: 0 new system files, ~5 brownfield-specific tuning files
**Dependencies**: ALL previous sprints

---

## Objective

Run the full Stagix pipeline end-to-end on a real project (greenfield + brownfield). Document gaps, fix issues, tune thresholds.

---

## Tickets

### STGX-063: Greenfield Integration Test
**Status**: TODO
**Description**: Complete end-to-end test using a simple Todo List API (Python FastAPI + PostgreSQL).

**Test Plan**:
1. Create a blank project directory
2. Run install.sh — verify setup completes
3. Run `/start-project 'A todo list API with user authentication'`
4. Verify detect-stack writes mode: greenfield
5. Follow BA elicitation — provide answers
6. `/approve business-analyst`
7. Verify PM produces PRD with epics
8. `/approve product-manager`
9. Verify UX Designer + Solution Architect run in parallel
10. `/approve ux-designer`, `/approve solution-architect`
11. Verify DB Designer produces schema
12. `/approve db-designer`
13. Verify Technical Writer publishes to Confluence
14. `/approve technical-writer`
15. Verify Scrum Master creates Jira epics + stories
16. Spot-check 5 stories for completeness
17. `/approve scrum-master` — Group 2 unlocked
18. Run `/implement-story TECH-3` (first story)
19. Verify Engineering Lead fetches from Jira, spawns Backend + Frontend Dev
20. Verify Backend Dev implements endpoints + tests
21. Verify Frontend Dev implements components + tests
22. `/approve devops`
23. Verify Test Case Specialist writes exhaustive test cases
24. `/approve test-plan`
25. Verify developers implement test cases
26. Verify Security Specialist produces audit report
27. `/approve security`
28. Verify Tech Lead reviews all 5 dimensions
29. `/approve tech-lead`
30. Verify QA Engineer starts dev server, runs Playwright tests
31. Verify screenshots saved to .stagix/qa/evidence/
32. `/approve qa`
33. `/approve final TECH-3`
34. Verify Jira status → Done

**Acceptance Criteria**:
- [ ] Complete end-to-end run with zero manual workarounds
- [ ] All Confluence pages created and cross-linked
- [ ] All Jira stories have full detail
- [ ] Git commit blocked until all gates pass
- [ ] Playwright QA runs successfully against dev server
- [ ] All gate files written and processed correctly

---

### STGX-064: Brownfield Integration Test
**Status**: TODO
**Description**: Test brownfield mode against an existing codebase.

**Test Plan**:
1. Use an existing FastAPI project as test brownfield codebase
2. Run `/discover-brownfield`
3. Verify Archaeologist produces comprehensive 12-section discovery report
4. Review and `/approve discovery`
5. Run `/start-project 'Add team management feature'`
6. Verify mode: brownfield set correctly
7. Verify all planning agents read brownfield-discovery.md as context
8. Verify PM uses brownfield-prd-tmpl.yaml
9. Verify Architect uses brownfield-architecture-tmpl.yaml
10. Verify SM uses brownfield-story-tmpl.yaml (rollback, regression risk, feature flag)
11. `/approve scrum-master`
12. Verify regression-baseline captured before first story
13. Run `/implement-story` on first brownfield story
14. Verify compatibility-check runs before code review
15. Verify tech debt items from Archaeologist feed into Security Specialist audit
16. Verify regression test suite doesn't drop below baseline
17. Complete full engineering pipeline

**Acceptance Criteria**:
- [ ] Archaeologist produces accurate discovery report
- [ ] Constrained planning agents respect existing architecture
- [ ] Brownfield story templates used with extra fields
- [ ] Regression baseline captured and enforced
- [ ] Compatibility check validates backward compatibility

---

### STGX-065: Edge Case Testing
**Status**: TODO
**Description**: Test failure paths and recovery.

**Scenarios**:
1. **Rejection flow**: Reject a planning agent, verify re-run with feedback
2. **3-strike escalation**: Force 3 consecutive Tech Lead failures, verify escalation triggers
3. **Session interruption**: Kill session mid-pipeline, restart, verify /status reconstructs state
4. **Unknown stack**: Point at a Haskell project, verify _generic.md fallback + overlay generation flag
5. **Rate limit handling**: Create project with 50+ stories, verify batch creation with pauses
6. **Dev server failure**: QA tries to start dev server that fails, verify graceful error in gate file

**Acceptance Criteria**:
- [ ] All 6 scenarios tested and passing
- [ ] Recovery paths work without manual intervention
- [ ] Error messages are clear and actionable

---

### STGX-066: Documentation & Tuning
**Status**: TODO
**Description**: Document any gaps found during integration testing. Tune thresholds. Update docs.

**Deliverables**:
- Update implementation-plan.md with actual findings
- Update feasibility-assessment.md with real-world results
- Tune coverage_threshold if 80% is too aggressive for initial stories
- Document any BMAD content that needed more adaptation than expected
- Create a CHANGELOG.md for v1.0

**Acceptance Criteria**:
- [ ] All gaps documented
- [ ] Thresholds tuned based on real usage
- [ ] CHANGELOG.md created

---

## Definition of Done (Entire Stagix v1.0)

- [ ] Greenfield full-stack project completes end-to-end
- [ ] Brownfield feature addition completes end-to-end
- [ ] All 13 human gates work correctly
- [ ] All 9 hooks fire and enforce correctly
- [ ] All 3 MCP servers integrated and working
- [ ] All 12 skill domains load correct overlays
- [ ] /status shows accurate pipeline state
- [ ] Session recovery works from file-based state
