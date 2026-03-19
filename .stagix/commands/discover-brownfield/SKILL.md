---
name: discover-brownfield
description: Manually trigger the Codebase Archaeologist for brownfield discovery
---

# /discover-brownfield

Triggers the Codebase Archaeologist in isolation. Useful when joining an existing project mid-stream.

## Usage
```
/discover-brownfield
```

## What Happens
1. Activate Codebase Archaeologist agent
2. Agent reads entire codebase (read-only — no modifications)
3. Produces `.stagix/docs/brownfield-discovery.md` (12-section report)
4. Gate file written for human review
5. Review with `/review-handoff discovery`, approve with `/approve discovery`
