# SQLite

## Specifics
- WAL mode for concurrent reads
- Single writer — plan accordingly
- No ALTER COLUMN — create new table, copy data, drop old
- PRAGMA journal_mode=WAL
- Suitable for: embedded, mobile, dev/test, low-write apps
