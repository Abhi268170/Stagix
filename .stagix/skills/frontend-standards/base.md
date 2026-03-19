# Frontend Standards — Universal Principles

These principles apply regardless of framework.

## Accessibility (WCAG 2.1 AA)
- All interactive elements keyboard-navigable (Tab, Enter, Escape, Arrow keys)
- ARIA labels on all non-text interactive elements
- Colour contrast: 4.5:1 for normal text, 3:1 for large text
- Focus indicators visible on all interactive elements
- Skip navigation link for screen readers
- Alt text on all images (empty alt="" for decorative images)
- Form labels associated with inputs (htmlFor/for attribute)

## Performance Budgets
- First Contentful Paint < 1.5s
- Largest Contentful Paint < 2.5s
- Total bundle size < 200KB gzipped (initial load)
- Images: use modern formats (WebP/AVIF), lazy load below fold
- Code splitting: route-based at minimum

## State Management
- Local state for component-specific UI state
- Global state only for truly shared data (auth, theme, notifications)
- Server state via data fetching library (react-query, SWR, etc.) — not global store
- URL state for anything that should be shareable/bookmarkable

## Component Design
- Single responsibility per component
- Props for configuration, slots/children for composition
- Controlled inputs for forms
- Error boundaries around feature sections
- Loading states for all async operations
- Empty states for lists/tables with no data

## Form Handling
- Inline validation (on blur, not on every keystroke)
- Clear error messages next to the field
- Preserve user input on validation failure
- Disable submit button during submission
- Show loading state during submission
- Success/error feedback after submission
