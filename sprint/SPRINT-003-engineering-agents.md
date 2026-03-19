# SPRINT-003: Phase 3 — Engineering Group Agents & Tasks

**Status**: DONE
**Priority**: P0 — Blocks story implementation
**Estimate**: ~17 files
**Dependencies**: SPRINT-001 (Foundation)

---

## Objective

Build all 8 engineering agents and their task files. After this phase, `/implement-story PROJ-123` can activate the Engineering Lead who spawns specialists through the full engineering pipeline.

---

## Tickets

### STGX-021: Engineering Lead Agent
**Status**: TODO
**File**: `.stagix/agents/engineering/engineering-lead.md`
**Description**: Orchestrator for Group 2. Uses subagent spawning (not Agent Teams). Fetches story from Jira, validates story-ready checklist, spawns specialists in sequence. Manages failure routing and 3-strike escalation.

**Tool Allowlist**: Task (spawn subagents), `jira_get_issue`, `jira_get_transitions`, `jira_search`, Read (.stagix/gates/*)
**Outputs**: Orchestration only — delegates all work to subagents

**Acceptance Criteria**:
- [ ] Fetches story from Jira via MCP
- [ ] Validates story-ready checklist (all 12 fields present)
- [ ] Blocks if Group 1 final gate not approved
- [ ] Spawns Backend+Frontend Dev in parallel where safe, sequential where dependent
- [ ] Routes review failures back to Dev with specific feedback
- [ ] Triggers 3-strike escalation after 3 consecutive failures from same reviewer

---

### STGX-022: Backend Developer Agent (James)
**Status**: TODO
**Files**:
- `.stagix/agents/engineering/backend-dev.md`
- `.stagix/tasks/engineering/implement-story.md`

**Description**: Implements backend tasks from the story. Loads architecture constraints as always-on context. Implements task by task, writes tests after each, validates before marking complete.

**Tool Allowlist**: Read, Write, Edit, Bash (run tests, linters, dev server). NO MCP access.
**Skills Loaded**: backend-standards (base + detected stack overlay), test-writing, scalability-patterns (on demand)
**devLoadAlwaysFiles**: coding-standards.md, tech-stack.md, source-tree.md

**BMAD Reuse**: From dev.md (~60%). Keep implementation discipline, task-by-task execution. Split out backend-specific concerns.

**Acceptance Criteria**:
- [ ] Reads story from Jira (via Engineering Lead context, not direct MCP)
- [ ] Loads devLoadAlwaysFiles before starting
- [ ] Follows strict order: Read task → Implement → Write tests → Run tests → Update File List → Mark checkbox
- [ ] Blocks on: unapproved dependency, ambiguity, 3 consecutive failures, missing config
- [ ] Can only modify: task checkboxes, Dev Agent Record, File List, Change Log

---

### STGX-023: Frontend Developer Agent (Jamie)
**Status**: TODO
**File**: `.stagix/agents/engineering/frontend-dev.md`

**Description**: Implements frontend tasks. References design-system/MASTER.md as immutable constraint. Runs ui-ux-pro-max pre-delivery checklist.

**Tool Allowlist**: Read, Write, Edit, Bash (npm run dev, npm test, npm run lint). NO MCP.
**Skills Loaded**: frontend-standards (base + detected framework overlay), ui-ux-pro-max (read-only design system reference), test-writing

**BMAD Reuse**: From dev.md (~60%). Split out frontend concerns. Add design system enforcement.

**Acceptance Criteria**:
- [ ] Reads design-system/MASTER.md before writing any component
- [ ] Flags to human if UI decision deviates from MASTER.md
- [ ] Runs pre-delivery checklist: no emoji icons, cursor-pointer, hover states, contrast ratios, focus states, prefers-reduced-motion, responsive breakpoints
- [ ] Same blocking conditions as backend dev

---

### STGX-024: DevOps Engineer Agent (Dev)
**Status**: TODO
**File**: `.stagix/agents/engineering/devops.md`

**Description**: Reviews implementation for infrastructure implications. Updates CI/CD, Docker, IaC as needed.

**Tool Allowlist**: Read, Write (.github/workflows/*.yml, docker-compose.yml, Dockerfile, terraform/**), Bash (docker build, terraform plan). NO application code. NO MCP.
**Skills Loaded**: infrastructure (base + detected CI/cloud overlay)

**Acceptance Criteria**:
- [ ] Reviews story for infra needs
- [ ] Updates CI pipeline if new test types added
- [ ] Updates Dockerfile if dependencies changed
- [ ] Cannot modify application code

---

### STGX-025: Test Case Specialist Agent (Quinn)
**Status**: TODO
**Files**:
- `.stagix/agents/engineering/test-case-specialist.md`
- `.stagix/tasks/engineering/write-test-cases.md`

**Description**: Reads story AC + edge cases. Writes exhaustive test plan BEFORE developers implement tests. Developers then implement exactly these cases.

**Tool Allowlist**: Read (story from Jira, coding-standards.md, ux-spec.md), Write (.stagix/tests/{story-key}-test-plan.md), `confluence_create_page`, `playwright__browser_generate_locator`
**Skills Loaded**: test-writing (base + detected testing framework overlay)

**BMAD Reuse**: Extract test-design capabilities from qa.md (~50%). Add Playwright locator generation, traceability matrix.

**Acceptance Criteria**:
- [ ] Given-When-Then format for every test case
- [ ] Playwright locator hints for UI interactions (if dev server running)
- [ ] Edge case coverage: empty states, error states, boundary values, concurrent access
- [ ] Traceability matrix linking each test case to specific AC item
- [ ] Published to Confluence 'Test Plan: PROJ-123'

---

### STGX-026: Security Specialist Agent (Ash)
**Status**: TODO
**Files**:
- `.stagix/agents/engineering/security-specialist.md`
- `.stagix/tasks/engineering/security-audit.md`

**Description**: Read-only code audit. Reviews against OWASP Top 10 + stack-specific vulnerabilities. CRITICAL/HIGH findings block the story.

**Tool Allowlist**: Read, Grep, Glob (read-only). `confluence_create_page`, `jira_add_comment`. **NO Write/Edit/Bash.**
**Skills Loaded**: security-review (base + detected language overlay — Python/Node/Rails/Java/PHP/Go)

**BMAD Reuse**: Extract risk/security concepts from qa.md (~40%). Focus on OWASP, add stack-specific patterns.

**Acceptance Criteria**:
- [ ] Reviews: SQL injection, XSS, CSRF, IDOR, secrets detection, auth patterns, input validation, dependency CVEs, error message leakage, rate limiting
- [ ] CRITICAL/HIGH findings → story blocked
- [ ] MEDIUM findings → noted, don't block
- [ ] LOW findings → documented as tech debt
- [ ] Cannot modify any code
- [ ] Publishes to Confluence 'Security Audit: PROJ-123'

---

### STGX-027: Tech Lead Reviewer Agent (Morgan)
**Status**: TODO
**Files**:
- `.stagix/agents/engineering/tech-lead-reviewer.md`
- `.stagix/tasks/engineering/code-review.md`

**Description**: The hardest gate. 5-dimension code review. Read-only. PASS/FAIL per dimension is binding.

**Tool Allowlist**: Read, Grep, Glob (read-only). `confluence_create_page`, `jira_add_comment`. **NO Write/Edit/Bash.**
**Skills Loaded**: code-review (base review standards + architecture conformance rules), security-review (cross-reference)

**5 Dimensions**:
1. Code Quality & Patterns — no shortcuts, no hacks, SOLID, naming, dead code
2. Security Conformance — cross-references Security Specialist report, all CRITICAL/HIGH resolved
3. Test Coverage — all Test Specialist cases implemented, coverage meets threshold
4. Architecture Conformance — matches architecture.md tech stack, coding standards, source tree
5. Performance & Scalability — N+1 queries, unbounded loops, missing pagination, cache opportunities

**Acceptance Criteria**:
- [ ] All 5 dimensions evaluated with PASS/FAIL
- [ ] Any FAIL → story returned to dev with specific findings
- [ ] Cross-references Security Specialist report
- [ ] Checks coverage threshold from core-config.yaml
- [ ] Cannot modify code
- [ ] Publishes to Confluence 'Code Review: PROJ-123'

---

### STGX-028: QA Engineer Agent (River)
**Status**: TODO
**Files**:
- `.stagix/agents/engineering/qa-engineer.md`
- `.stagix/tasks/engineering/run-playwright-tests.md`

**Description**: Browser-based acceptance testing via Playwright MCP. Starts dev server, navigates to application, verifies each AC item against real browser behaviour.

**Tool Allowlist**: Read (story, test plan), Bash (dev server startup from core-config.yaml), all `mcp__playwright__browser_*` tools, `confluence_create_page`, `jira_update_issue`, `jira_add_comment`. **Cannot write application code.**
**Skills Loaded**: test-writing (for understanding test case format)

**BMAD Reuse**: None — entirely new. BMAD QA is code-review only.

**Acceptance Criteria**:
- [ ] Starts dev server using command from core-config.yaml
- [ ] Waits for health check endpoint
- [ ] For each AC: navigate → interact → verify → screenshot
- [ ] Edge cases tested
- [ ] Regression: verifies core user journeys from previous stories
- [ ] QA report with PASS/FAIL per AC + evidence links + console errors
- [ ] Traces and screenshots saved to .stagix/qa/evidence/
- [ ] Published to Confluence 'QA Evidence: PROJ-123'

---

### STGX-029: Supporting Engineering Tasks
**Status**: TODO
**Files**:
- `.stagix/tasks/engineering/implement-tests.md` — Dev's protocol for implementing Test Specialist's cases
- `.stagix/tasks/engineering/update-jira-status.md` — Status transition via Atlassian MCP (used by hooks)
- `.stagix/tasks/engineering/story-dod-check.md` — Developer self-check before marking complete
- `.stagix/tasks/brownfield/compatibility-check.md` — Validates new code doesn't break existing APIs/schema
- `.stagix/tasks/brownfield/brownfield-impact-assess.md` — Before any story: what does this change touch?

**Acceptance Criteria**:
- [ ] implement-tests.md follows exact test cases from Test Specialist
- [ ] update-jira-status.md handles all transitions: Planned → In Dev → In Review → Done
- [ ] story-dod-check.md maps to story-dod-checklist.md items
- [ ] compatibility-check validates API backward compatibility
- [ ] brownfield-impact-assess runs before story enters dev

---

## Smoke Test (Phase 3 Complete)

1. Run `/implement-story` with a pre-existing Jira story
2. Verify Engineering Lead fetches story and validates fields
3. Verify Backend Dev activates and loads devLoadAlwaysFiles
4. Verify gate files written after each engineering agent completes

## Definition of Done

- [ ] All 9 tickets completed (STGX-021 through STGX-029)
- [ ] All agents have correct tool allowlists matching external-tool-access-map.md
- [ ] Engineering Lead spawns agents in correct sequence per blueprint Section 5.9
- [ ] Security → Tech Lead → QA are strictly sequential
