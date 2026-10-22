# Data Processing Capstone

## Objective
Combine collection processing and an API adapter to generate a JSON report and handle recoverable failures.

## Features
- Fetches JSON records from an API.
- Validates and processes collection records.
- Separates valid and rejected records.
- Handles network errors and invalid JSON.
- Uses sample data when the API is unavailable.
- Saves processing results as a JSON report.
- Includes automated tests for success, failure, and boundary cases.

## Project Structure
- src/data_processor.py — validates and processes records.
- src/api_client.py — fetches API data and handles failures.
- src/report_generator.py — saves JSON reports.
- tests/ — automated test suite.
- main.py — application entry point.
- design_notes.md — design decisions and limitations.

## Requirements
- Python 3.12 or compatible Python 3 version.
- pytest for automated tests.
- Internet access for live API requests; tests use mocked responses.

## Run the Application
From the project root:

bash
python main.py


The report is saved to output/report.json.

## Run Tests
Install pytest if required:

bash
python -m pip install pytest


Run all tests:

bash
python -m pytest -v


## Verification Evidence
- Application successfully fetched 200 API records.
- 200 records processed and 0 rejected in the successful run.
- All 9 automated tests passed.
- Tests cover valid data, invalid data, empty collections, network failure, invalid JSON, report creation, and report-writing failure.

## Known Limitations
- The application uses a fixed API endpoint.
- Sample data is used when the API request fails.
- Reports are written as JSON; historical reports are not maintained.
- The application does not retry failed API requests.