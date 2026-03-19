---
name: api-design
description: API design principles, contracts, and versioning
---

# Skill Loader: api-design

## Loading Algorithm

1. Read `.stagix/core-config.yaml` → extract `detected_stack` relevant to this domain
2. Load `base.md` from this directory — universal principles that always apply
3. Check `stacks/{detected_framework}.md` exists:
   - If found → load it (stack-specific rules)
   - If not found → load `stacks/_generic.md` + flag for Solution Architect to generate overlay
4. Present unified context to the agent:
   - "Universal rules from base.md apply everywhere."
   - "Stack-specific rules from {framework}.md apply to {framework} components."
5. If multi-stack project (e.g., Python backend + Next.js frontend):
   - Load both relevant overlays
   - Annotate which overlay applies to which part of the codebase
