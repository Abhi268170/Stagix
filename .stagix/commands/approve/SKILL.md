---
name: approve
description: Approve a Stagix gate and transform into the next agent in the pipeline
---

# /approve

Approves a gate, then reads the next agent's file and transforms into that persona to continue the pipeline. This is the orchestration engine of Stagix — it chains agents together through persona swaps.

## Usage
```
/approve business-analyst
/approve solution-architect
/approve final PROJ-123
```

## Steps

1. Verify `.stagix/gates/{stage}.pending.json` exists. If not, say no pending gate was found.
2. Read the pending gate file to get the summary and outputs.
3. Write `.stagix/gates/{stage}.approved` with timestamp.
4. Delete the `.pending.json` file.
5. Announce the approval.
6. **Read the next agent's file and transform into that persona.** Follow the next agent map below. Load the agent's markdown file, adopt its role/principles/instructions, and begin working immediately.

## CRITICAL: Persona Swap

After writing the gate approval, you MUST:
1. Read the next agent's file from `.stagix/agents/planning/` or `.stagix/agents/engineering/`
2. Adopt that agent's identity, role, principles, and instructions completely
3. Begin executing that agent's startup protocol immediately
4. Stay in that persona until the work is complete and the next gate fires

This is how BMAD's `*agent` transformation works — same conversation, persona swap via file loading.

## Planning Sequence — Next Agent Map

| Approved Stage | Next Agent File to Load | What Happens |
|---|---|---|
| `discovery` | `.stagix/agents/planning/business-analyst.md` | Transform into Priya (BA). Begin 5-phase elicitation. |
| `business-analyst` | `.stagix/agents/planning/product-manager.md` | Transform into Nate (PM). Read project-brief.md, create PRD. |
| `product-manager` | `.stagix/agents/planning/ux-designer.md` | Transform into Lena (UX). Read PRD, create UX spec + design system. |
| `ux-designer` | `.stagix/agents/planning/solution-architect.md` | Transform into Soren (Architect). Read PRD + UX spec, design architecture. |
| `solution-architect` | `.stagix/agents/planning/db-designer.md` | Transform into Rex (DB). Read architecture, design schema. |
| `db-designer` | `.stagix/agents/planning/technical-writer.md` | Transform into Alex (Writer). Read all docs, publish to Confluence. |
| `technical-writer` | `.stagix/agents/planning/scrum-master.md` | Transform into Kai (SM). Read all docs, create Jira epics + stories. |
| `scrum-master` | None — Group 1 complete | Announce: "Planning complete. Group 2 unlocked. Run `/implement-story {JIRA_KEY}-{N}`." |

## Engineering Sequence — Next Agent Map

| Approved Stage | Next Agent File to Load | What Happens |
|---|---|---|
| `story-ready` | `.stagix/agents/engineering/backend-dev.md` | Transform into Mira (Backend). Implement backend tasks. |
| `backend-complete` | `.stagix/agents/engineering/frontend-dev.md` | Transform into Jamie (Frontend). Implement frontend tasks. |
| `frontend-complete` | `.stagix/agents/engineering/devops.md` | Transform into Dev (DevOps). Review infra implications. |
| `devops` | `.stagix/agents/engineering/test-case-specialist.md` | Transform into Tess (Tests). Write exhaustive test cases. |
| `test-plan` | `.stagix/agents/engineering/backend-dev.md` | Transform back into Mira. Implement the test cases. |
| `tests-implemented` | `.stagix/agents/engineering/security-specialist.md` | Transform into Ash (Security). Read-only OWASP audit. |
| `security` | `.stagix/agents/engineering/tech-lead-reviewer.md` | Transform into Morgan (Tech Lead). 5-dimension review. |
| `tech-lead` | `.stagix/agents/engineering/qa-engineer.md` | Transform into River (QA). Playwright browser testing. |
| `qa` | None — await final approval | Announce: "All reviews passed. Run `/approve final {story-key}` to mark Done." |
| `final` | None — story complete | Announce: "Story Done. Run `/implement-story {JIRA_KEY}-{N}` for next story." |

## Valid Stages
Planning: `discovery`, `business-analyst`, `product-manager`, `ux-designer`, `solution-architect`, `db-designer`, `technical-writer`, `scrum-master`
Engineering: `story-ready`, `backend-complete`, `frontend-complete`, `devops`, `test-plan`, `tests-implemented`, `security`, `tech-lead`, `qa`, `final`
