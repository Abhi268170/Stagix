# Task: brownfield-impact-assess

## Purpose

Before any story enters development in brownfield mode: analyse what this change touches and what the blast radius is.

## Protocol

1. Read the story's "Existing Code Affected" section
2. For each file listed:
   - How many other files import/depend on it?
   - Is it covered by tests? What's the coverage?
   - Is it flagged as tech debt in the discovery report?
   - How recently was it last modified? (stable or actively changing)
3. Map the dependency chain:
   - If we change file A, what files B, C, D are affected?
   - Are any of those files in other stories/epics being developed in parallel?
4. Assess overall impact:
   - **Low**: Change is isolated, well-tested area, no shared dependencies
   - **Medium**: Touches shared code but has test coverage
   - **High**: Touches shared code with low coverage or known tech debt

## Output

Impact assessment summary provided to the Engineering Lead before spawning developers. If impact is HIGH, Engineering Lead should flag to human before proceeding.
