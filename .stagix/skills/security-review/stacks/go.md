# Go Security

## Stack-Specific Risks
- Goroutine leaks: always cancel contexts, close channels
- Race conditions: go test -race, sync.Mutex or channels
- SQL injection: use database/sql prepared statements
- Template injection: html/template auto-escapes (not text/template)
- Integer overflow: bounds check before casting
