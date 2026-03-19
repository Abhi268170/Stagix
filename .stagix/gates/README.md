# Gate Files

Gate files are the human approval mechanism in Stagix. Every agent boundary has a gate. No agent proceeds without explicit human approval.

## File Types

### `{stage}.pending.json`

Written automatically by the `handoff-gate.py` Stop hook when an agent completes. Contains everything the human needs to review.

```json
{
  "stage": "solution-architect",
  "agent": "Winston (Solution Architect)",
  "completed_at": "2026-03-18T14:32:00Z",
  "summary": "Completed full-stack architecture for Stagix Demo Project...",
  "outputs": [
    ".stagix/docs/architecture.md",
    ".stagix/docs/architecture/coding-standards.md",
    ".stagix/docs/architecture/tech-stack.md",
    ".stagix/docs/architecture/source-tree.md"
  ],
  "confluence_pages": [
    "https://...atlassian.net/wiki/..."
  ],
  "next_agent": "db-designer",
  "review_questions": [
    "Does the proposed microservices boundary match your deployment constraints?",
    "Is PostgreSQL acceptable or do you need to consider an existing database?"
  ],
  "concerns_flagged": [
    "No existing caching layer — Redis was proposed"
  ],
  "approval_command": "/approve solution-architect",
  "reject_command": "/reject solution-architect \"your feedback\""
}
```

### `{stage}.approved`

Written by the `/approve {stage}` command. A simple text file confirming approval.

```
approved_at: 2026-03-18T15:00:00Z
approved_by: human
note: Architecture looks good. Proceed with PostgreSQL.
```

The presence of this file is what unlocks the next agent. The next agent's startup (or the orchestrator) checks for `{previous_stage}.approved` before proceeding.

### `{stage}.rejected`

Written by the `/reject {stage} "reason"` command. Contains feedback that gets routed to the agent for rework.

```
rejected_at: 2026-03-18T15:00:00Z
rejected_by: human
reason: Need to use existing Redis, not new. Also missing rate limiting in API design.
```

When a rejection file is written:
1. The `.pending.json` file is deleted (to allow re-submission)
2. The orchestrator reads the rejection reason
3. The completing agent is re-activated with the feedback injected as context
4. The agent re-runs, producing updated output
5. A new `.pending.json` is written on completion

## Gate Sequence

### Planning Group (8 gates)
1. `business-analyst` → 2. `product-manager` → 3. `ux-designer` → 4. `solution-architect` → 5. `db-designer` → 6. `technical-writer` → 7. `scrum-master`

Gate 7 (`scrum-master`) is the **final Group 1 gate**. Its approval unlocks Group 2 (Engineering Collective).

### Engineering Group (6 gates per story)
8. `devops` → 9. `test-plan` → 10. `security` → 11. `tech-lead` → 12. `qa` → 13. `final`

Gate 13 (`final`) is the **merge decision** for each story.

## 3-Strike Escalation

If a story accumulates 3 consecutive FAIL outcomes from any single review agent (Security, Tech Lead, or QA):
- Story status is set to `Blocked` in Jira
- A Confluence page `Escalation: PROJ-123` is created with the full failure log
- A desktop notification is sent
- Human intervention is required before the Engineering Lead can proceed
