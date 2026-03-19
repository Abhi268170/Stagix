# PHP Security

## Stack-Specific Risks
- Type juggling: use === not == for comparisons
- RFI/LFI: never include files from user input
- SQL injection: PDO prepared statements always
- Session fixation: regenerate session ID after login
- File uploads: validate MIME type server-side, not just extension
