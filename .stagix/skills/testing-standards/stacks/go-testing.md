# Go Testing

## Conventions
- Table-driven tests ([]struct with test cases)
- t.Run for subtests
- testify/assert for assertions (optional)
- httptest for HTTP handler testing
- sqlmock for database testing
- go test -race for race condition detection
