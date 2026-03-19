# Jest + React Testing Library

## Conventions
- render() + screen queries (getByRole preferred over getByTestId)
- userEvent over fireEvent for realistic interactions
- waitFor for async assertions
- Mock API calls with MSW (Mock Service Worker)
- Snapshot tests sparingly (only for stable UI)
