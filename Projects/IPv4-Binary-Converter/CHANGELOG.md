# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2025-05-26

### Fixed
- Input validation bug where program would exit unexpectedly after first conversion if user entered anything other than 'y' or 'yes'
- Added consistent input validation for all yes/no prompts using new `get_yes_no_response()` function

### Added
- Type hints for better code documentation
- `__init__.py` file for proper package structure
- This CHANGELOG file

### Technical Details
- Bug was caused by missing validation on the continuation prompt after first conversion
- Solution implements DRY principle with reusable validation function
- All user inputs now consistently use `.strip().lower()` and validate against allowed responses

## [1.0.0] - 2024-09-07 (Original Submission)

### Features
- Convert decimal IPv4 addresses to binary format
- Comprehensive input validation
- User-friendly CLI with multiple exit options
- Modular code architecture with separate validation and conversion modules
- Continuous conversion capability
- Clear error messages and graceful error handling