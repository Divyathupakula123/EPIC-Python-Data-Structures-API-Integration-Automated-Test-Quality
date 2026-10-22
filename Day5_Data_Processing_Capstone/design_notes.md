# Design Notes — Data Processing Capstone

## 1. Design Overview
The application is divided into separate modules to keep API communication, data processing, and report generation independent.

## 2. Module Responsibilities
- api_client.py: Fetches JSON data and handles HTTP, network, timeout, and invalid JSON errors.
- data_processor.py: Validates records and separates valid records from rejected records.
- report_generator.py: Writes the processing report to a JSON file.
- main.py: Coordinates the workflow and uses sample data when the API is unavailable.

## 3. Design Decisions
- Python standard-library modules are used for API requests and JSON handling.
- Each module has one main responsibility, making the code easier to test and maintain.
- Invalid records are rejected individually so that other valid records can still be processed.
- API requests are mocked in automated tests to avoid external network dependencies.
- pathlib is used for file paths and report output.

## 4. Failure and Recovery Behavior
- Network and HTTP errors are returned as structured error results.
- Invalid JSON responses are handled without crashing the API adapter.
- Invalid records are recorded with rejection reasons.
- If the API fails during the main workflow, sample data is processed instead.
- Report-writing errors are returned to the caller.

## 5. Testing Strategy
Automated tests cover:
- Valid records.
- Invalid records and empty collections.
- Network failure.
- Invalid JSON.
- Successful report creation.
- Report-writing failure.

## 6. Verification
The application successfully fetched 200 API records during a live run.
The current automated test suite completed with 9 passing tests.

## 7. Known Limitations
- The API endpoint is configured directly in the source code.
- Sample data is used as a fallback rather than retrying the API.
- Reports are saved as JSON, with no database or historical report tracking.
- CI execution must be verified separately in the configured CI environment.

## 8. Future Improvements
- Move the API endpoint into configuration.
- Add retry and backoff handling.
- Add structured logging.
- Add CI automation for all tests.