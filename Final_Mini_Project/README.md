# Reliable Data Processing Utility with API Adapter

## Objective
Build a reliable Python utility that validates CSV records,
processes valid data, handles API failures, and records logs.

## Technologies
- Python 3.12
- CSV and JSON
- Requests
- Pytest
- Logging

## Project Structure
- src/processor.py - CSV validation and processing
- src/api_client.py - API requests and failure handling
- src/main.py - Application workflow
- tests/ - Automated tests
- data/input.csv - Sample input data
- reports/ - Generated outputs and logs

## Setup
Activate the project's virtual environment and install dependencies:

    python -m pip install -r requirements.txt

## Run the Application

    python .\src\main.py

Optional API request:

    python .\src\main.py --api-url "YOUR_TEST_API_URL"

Use only a safe development/test API endpoint.

## Run Tests

    python -m pytest tests -v

## Validation Rules
- Required columns: id, name, amount
- Empty values are rejected
- Duplicate IDs are rejected
- Negative amounts are rejected
- Valid records are written to processed.csv

## Error Handling
- Missing input files raise FileNotFoundError
- Invalid CSV headers raise ValueError
- API timeouts and request failures are handled
- Application events are written to application.log

## Test Evidence
Record the actual pytest output and application results
before final delivery.

## Known Limitations
- API response data is saved separately; it is not yet
  merged with the CSV processing workflow.
- Retry logic and restart recovery are not implemented.
- The current tests use mocked API responses.

## Security
Do not commit API keys, credentials, or sensitive data.