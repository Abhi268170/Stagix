---
name: approve
description: Approve a Stagix gate, unlocking the next agent in the pipeline
---

# /approve

Approves a gate and tells the user which agent to activate next.

## Usage
```
/approve business-analyst
/approve solution-architect
/approve final PROJ-123
```

## Steps

1. Verify `.stagix/gates/{stage}.pending.json` exists. If not, tell the user no pending gate was found for that stage.
2. Read the pending gate file to get the summary and outputs.
3. Write `.stagix/gates/{stage}.approved` with timestamp and any approval note.
4. Delete the `.pending.json` file.
5. Tell the user the gate is approved and **which agent to activate next**.

## Planning Sequence — Next Agent Map

After approving a planning gate, tell the user exactly what to do next:

| Approved Stage | Next Step |
|---|---|
| `discovery` | "Discovery approved. Now activate the **business-analyst** agent with your project idea." |
| `business-analyst` | "BA approved. Now activate the **product-manager** agent. It will read the project brief and create the PRD." |
| `product-manager` | "PM approved. Now activate the **ux-designer** agent. It will read the PRD and create the UX spec + design system." |
| `ux-designer` | "UX approved. Now activate the **solution-architect** agent. It will read the PRD + UX spec and design the system architecture." |
| `solution-architect` | "Architect approved. Now activate the **db-designer** agent. It will read the architecture and design the database schema." |
| `db-designer` | "DB design approved. Now activate the **technical-writer** agent. It will publish all documents to Confluence." |
| `technical-writer` | "Technical Writer approved. Now activate the **scrum-master** agent. It will create Jira epics and stories from all design docs." |
| `scrum-master` | "Scrum Master approved. **Group 1 (Planning) is complete.** Group 2 (Engineering) is now unlocked. Run `/implement-story {JIRA_KEY}-{N}` to start engineering on any story." |

## Engineering Sequence — Next Agent Map

Engineering agents run as subagents (spawned by the Engineering Lead), so the user just approves and the pipeline continues automatically:

| Approved Stage | Next Step |
|---|---|
| `devops` | "DevOps approved. Test Case Specialist will activate next." |
| `test-plan` | "Test plan approved. Developers will implement the test cases, then Security review begins." |
| `security` | "Security approved. Tech Lead review begins next." |
| `tech-lead` | "Tech Lead approved. QA Engineer begins browser testing next." |
| `qa` | "QA approved. Run `/approve final {story-key}` for final merge approval." |
| `final` | "Story approved and marked Done. Run `/implement-story {JIRA_KEY}-{N}` for the next story." |

## Valid Stages
Planning: `discovery`, `business-analyst`, `product-manager`, `ux-designer`, `solution-architect`, `db-designer`, `technical-writer`, `scrum-master`
Engineering: `devops`, `test-plan`, `security`, `tech-lead`, `qa`, `final`
