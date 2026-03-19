---
name: review-handoff
description: Display the pending gate file for a completed agent's output
---

# /review-handoff

Shows what an agent produced and what needs human review.

## Usage
```
/review-handoff business-analyst
/review-handoff tech-lead
```

## What Happens
1. Read `.stagix/gates/{stage}.pending.json`
2. Display formatted summary:
   - What agent completed
   - Output files produced
   - Confluence pages created
   - Review questions from the agent
   - Concerns flagged
3. Show /approve and /reject commands
