# MySQL/MariaDB

## Specifics
- InnoDB engine (never MyISAM for new tables)
- utf8mb4 charset (not utf8 — it's only 3 bytes)
- EXPLAIN ANALYZE for query optimisation
- Covering indexes for read-heavy queries
- Generated columns for computed fields
