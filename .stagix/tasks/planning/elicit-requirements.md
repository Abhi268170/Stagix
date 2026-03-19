# Task: elicit-requirements

## Purpose

Structured 5-phase elicitation protocol for the Business Analyst. Transforms a vague project idea into a validated, documented set of requirements. This task is interactive — every phase involves human Q&A.

## Prerequisites

- User has provided a project idea (via `/start-project "idea"`)
- core-config.yaml has been populated by detect-stack
- If brownfield: brownfield-discovery.md exists

## The 5 Phases

Execute each phase sequentially. Do not skip phases. Do not combine phases. Each phase produces specific outputs that feed the next.

### Phase 1: Goal Clarification (3-5 questions minimum)

Ask:
- What is the core problem being solved?
- Who experiences this problem most acutely?
- What does success look like in 6 months?
- What happens if this isn't built?

Follow up with at least 3 probing "why" questions based on initial answers. Dig deeper until the underlying need is clear, not just the surface request.

### Phase 2: User Identification (2-4 questions minimum)

Ask:
- Who are the primary users? (Roles, not names)
- What are their daily goals and frustrations?
- Are there admin/operator roles separate from end users?
- What is each user type's technical sophistication?

Build 2-3 preliminary user personas with: Name, Role, Goals, Pain Points, Tech Comfort.

### Phase 3: Problem Validation (3-5 questions minimum)

Ask:
- Is this a real observed problem or an assumed one?
- How is it currently being solved? (Workarounds, manual processes)
- What are the constraints? (Budget, team size, timeline)
- Are there regulatory or compliance requirements?
- What are the risks of solving it wrong?

### Phase 4: Scope Boundary Setting (3-5 questions minimum)

Ask:
- What is IN scope for the first version?
- What is explicitly OUT of scope? (Just as important)
- What are the must-have features vs nice-to-haves?

Apply MoSCoW prioritisation:
- **Must Have**: Without these, the product doesn't work
- **Should Have**: Important but the product works without them
- **Could Have**: Nice to have if time permits
- **Won't Have (this time)**: Explicitly deferred

### Phase 5: Success Criteria (2-4 questions minimum)

Ask:
- How will we measure success? (Specific, quantifiable metrics)
- What is the minimum viable outcome?
- Timeline expectations?

Summarise all decisions from all 5 phases and get explicit human confirmation: "Does this accurately capture your requirements?"

## Advanced Elicitation (Optional, Per Phase)

After each phase, offer the human advanced elicitation techniques:

```
Advanced Elicitation Options (choose 0-8, or 9 to proceed):
0. Expand or Contract — Broaden or narrow scope
1. Explain Reasoning — Walk through logic
2. Critique and Refine — Challenge assumptions
3. Identify Risks — What could go wrong?
4. Assess Goal Alignment — Does this fit objectives?
5. Tree of Thoughts — Explore multiple paths
6. Stakeholder Roundtable — Multiple user perspectives
7. Hindsight Reflection — If this failed, what would we wish we'd considered?
8. Competitive Context — What do similar products do?
9. Proceed to next phase
```

## Brownfield Adjustment

In brownfield mode, frame all questions in context of the existing system:
- Phase 1: "Given the existing system does X, what ADDITIONAL problem are we solving?"
- Phase 3: "How does the existing system currently handle this?"
- Phase 4: "Which existing features are affected by this change?"

## Output

Feed all elicitation results into the `create-project-brief` task to produce `.stagix/docs/project-brief.md`.

Include an Elicitation Log section documenting key decisions from each phase.
