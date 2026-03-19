---
name: approve
description: Approve a Stagix gate, unlocking the next agent in the pipeline
---

# /approve

Writes a gate approval file, unlocking the next agent.

## Usage
```
/approve solution-architect
/approve final PROJ-123
```

## What Happens
1. Verify `.stagix/gates/{stage}.pending.json` exists
2. Write `.stagix/gates/{stage}.approved` with timestamp
3. Delete the `.pending.json` file
4. Print: "{stage} approved. Next agent: {next}"

## Valid Stages
Planning: business-analyst, product-manager, ux-designer, solution-architect, db-designer, technical-writer, scrum-master, discovery (brownfield)
Engineering: devops, test-plan, security, tech-lead, qa, final
