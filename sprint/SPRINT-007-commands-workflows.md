# SPRINT-007: Phase 7+8 — Slash Commands & Workflow Definitions

**Status**: DONE
**Priority**: P1 — Human entry points + orchestration sequencing
**Estimate**: ~13 files
**Dependencies**: SPRINT-002, SPRINT-003 (Agents), SPRINT-005 (Hooks for gate system)

---

## Objective

Build all 7 slash commands and 6 workflow definitions. After this phase, humans can run `/start-project`, `/implement-story`, `/approve`, `/reject`, `/review-handoff`, `/status`, and `/discover-brownfield`. Orchestrators can read workflow YAML to determine agent sequencing.

---

## Tickets

### STGX-055: /start-project Command
**Status**: TODO
**File**: `.stagix/commands/start-project/SKILL.md`
**Description**: Main entry point for new projects. Triggers detect-stack, determines mode (greenfield/brownfield), activates Planning Lead.

**Behaviour**:
1. Accept project idea as argument (e.g., `/start-project 'A SaaS project management tool'`)
2. Run detect-stack task → writes mode + detected_stack to core-config.yaml
3. If brownfield: activate Codebase Archaeologist first
4. Activate Planning Lead with appropriate workflow YAML
5. Planning Lead takes over from here

---

### STGX-056: /implement-story Command
**Status**: TODO
**File**: `.stagix/commands/implement-story/SKILL.md`
**Description**: Entry point for engineering. Fetches story from Jira, validates prerequisites, activates Engineering Lead.

**Behaviour**:
1. Accept Jira key as argument (e.g., `/implement-story PROJ-123`)
2. Verify Group 1 final gate (scrum-master.approved) exists
3. Fetch story from Jira via `jira_get_issue`
4. Run story-ready checklist validation
5. Activate Engineering Lead with story context

---

### STGX-057: /approve Command
**Status**: TODO
**File**: `.stagix/commands/approve/SKILL.md`
**Description**: Human approval gate. Writes .approved file, unlocks next agent.

**Behaviour**:
1. Accept stage name (e.g., `/approve solution-architect`)
2. Verify .pending.json exists for that stage
3. Write .stagix/gates/{stage}.approved with timestamp and approval note
4. Print confirmation: '{stage} approved. Next agent: {next_agent}'

---

### STGX-058: /reject Command
**Status**: TODO
**File**: `.stagix/commands/reject/SKILL.md`
**Description**: Human rejection with feedback routing.

**Behaviour**:
1. Accept stage + reason (e.g., `/reject scrum-master "PROJ-12 missing rollback procedure"`)
2. Write .stagix/gates/{stage}.rejected with feedback
3. Print confirmation: '{stage} rejected. Feedback will be provided to {agent} on re-activation.'
4. Delete .pending.json to allow re-submission

---

### STGX-059: /review-handoff Command
**Status**: TODO
**File**: `.stagix/commands/review-handoff/SKILL.md`
**Description**: Shows pending gate file in readable format.

**Behaviour**:
1. Accept stage name (e.g., `/review-handoff business-analyst`)
2. Read .stagix/gates/{stage}.pending.json
3. Display: what agent produced, output files, Confluence links, review questions, concerns flagged
4. Show /approve and /reject commands

---

### STGX-060: /status Command
**Status**: TODO
**File**: `.stagix/commands/status/SKILL.md`
**Description**: Shows current pipeline state.

**Behaviour**:
1. Read .stagix/state/pipeline-log.json for pipeline history
2. Read .stagix/gates/ for pending/approved/rejected gates
3. Read .stagix/state/active-agent.json for current agent
4. Call `jira_search` for current sprint story statuses (if Jira configured)
5. Display: active agent, pending gates, approved gates, story statuses, open review items

---

### STGX-061: /discover-brownfield Command
**Status**: TODO
**File**: `.stagix/commands/discover-brownfield/SKILL.md`
**Description**: Manually triggers Archaeologist in isolation. Useful when joining existing project mid-stream.

**Behaviour**:
1. Activate Codebase Archaeologist agent
2. Archaeologist reads entire codebase
3. Produces brownfield-discovery.md
4. Gate file written for human review

---

### STGX-062: Workflow Definitions
**Status**: TODO
**Files** (6 total):
- `workflows/greenfield-fullstack.yaml`
- `workflows/greenfield-service.yaml`
- `workflows/greenfield-ui.yaml`
- `workflows/brownfield-fullstack.yaml`
- `workflows/brownfield-service.yaml`
- `workflows/brownfield-ui.yaml`

**Description**: YAML files defining end-to-end agent sequences for each project type and mode. Read by orchestrators (Planning Lead, Engineering Lead) to determine agent activation order.

**BMAD Reuse**: ~60% structure from BMAD workflow YAMLs. Add gate references, parallel execution markers, Group 1→2 sequencing.

**Acceptance Criteria**:
- [ ] Each workflow lists agents in correct order
- [ ] Parallel agents marked (UX + Architect)
- [ ] Gate references for each step
- [ ] Brownfield workflows include Archaeologist as first step
- [ ] greenfield-service.yaml skips UX Designer
- [ ] greenfield-ui.yaml skips backend architecture

---

## Smoke Test

1. Run `/status` — verify it reads pipeline-log.json
2. Run `/start-project 'test'` — verify detect-stack runs and Planning Lead activates
3. Run `/approve` and `/reject` — verify gate files written correctly

## Definition of Done

- [ ] All 8 tickets completed (STGX-055 through STGX-062)
- [ ] All 7 slash commands functional
- [ ] All 6 workflow definitions valid YAML
- [ ] /approve writes .approved, /reject writes .rejected
- [ ] /status displays meaningful output
