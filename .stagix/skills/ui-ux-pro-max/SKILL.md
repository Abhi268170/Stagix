---
name: ui-ux-pro-max
description: Industry-specific design system generation with 161 rules, 67 styles, 161 palettes, 57 font pairings
---

# UI UX Pro Max Skill

This skill wraps the externally installed `uipro-cli` tool. Install with:
```
npm install -g uipro-cli && uipro init --ai claude
```

## Activation

When loaded by the UX Designer agent:
1. Analyse the PRD to detect product category (SaaS, e-commerce, healthcare, etc.)
2. Run the Python reasoning engine (scripts/search.py) against the data files
3. Generate a complete design system: style, colour palette, typography pairing, key effects
4. Include anti-patterns to avoid for the detected product category
5. Output feeds into design-system/MASTER.md

## Pre-Delivery Checklist

Frontend Developer references this before marking tasks complete:
- No emoji icons as functional UI elements
- cursor-pointer on all clickables
- Hover states on all interactive elements
- Contrast ratios WCAG AA (4.5:1 text, 3:1 large)
- Focus states visible
- prefers-reduced-motion respected
- Responsive: 375px, 768px, 1024px, 1440px
