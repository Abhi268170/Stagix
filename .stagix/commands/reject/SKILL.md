---
name: reject
description: Reject a Stagix gate with feedback, routing the agent for rework
---

# /reject

Writes a rejection file with feedback. The agent will re-run with your feedback.

## Usage
```
/reject scrum-master "PROJ-12 missing rollback procedure"
/reject tech-lead "N+1 query in order listing must be resolved"
```

## What Happens
1. Write `.stagix/gates/{stage}.rejected` with feedback
2. Delete `.pending.json` (allows re-submission)
3. Print: "{stage} rejected. Agent will re-run with your feedback."
4. When the orchestrator re-activates the agent, the rejection feedback is injected as context

## Arguments
- First: stage name
- Second: feedback reason (in quotes)
