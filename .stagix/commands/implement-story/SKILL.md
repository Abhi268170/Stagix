---
name: implement-story
description: Launch the Engineering Collective for a specific Jira story
---

# /implement-story

Fetches a story from Jira and runs the full engineering pipeline.

## Usage
```
/implement-story PROJ-123
```

## What Happens
1. Verify Group 1 final gate (scrum-master.approved) exists
2. Fetch story from Jira via `mcp__atlassian__jira_get_issue`
3. Validate story-ready checklist (all required fields present)
4. Activate Engineering Lead agent
5. Engineering Lead spawns specialists in sequence

## Arguments
- First argument: Jira story key (e.g., PROJ-123)

## Prerequisites
- Group 1 (Planning Collective) must be complete and approved
- Story must exist in Jira with all required fields
