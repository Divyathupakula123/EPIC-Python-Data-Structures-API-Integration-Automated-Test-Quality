# Project Architecture

## Project Name
Reliable Data Processing Utility with API Adapter

## Objective
To validate CSV records, process valid data, handle API failures, and generate reports.

## Architecture Flow

text
Input CSV File
      |
      v
CSV Processor
      |
      v
Data Validation
      |
      +----> Invalid Records
      |
      v
Valid Records
      |
      v
Processed CSV
      |
      v
Summary JSON Report

Optional API URL
      |
      v
API Client
      |
      v
Validate API Response
      |
      v
API Response JSON

All application events
      |
      v
Application Log


## Main Components

- src/processor.py: Reads CSV data and validates records.
- src/api_client.py: Fetches JSON data and handles API errors.
- src/main.py: Coordinates processing and generates reports.
- tests/: Contains automated unit and integration tests.
- data/input.csv: Sample input data.
- reports/: Stores generated output files and logs.

## Data Validation Rules

1. Required columns are id, name, and amount.
2. Empty required values are rejected.
3. Duplicate IDs are rejected.
4. Negative amounts are rejected.
5. Valid records are saved to processed.csv.

## Error Handling

- Missing input file: FileNotFoundError
- Invalid CSV columns: ValueError
- API timeout or request failure: RuntimeError

## Testing Strategy

Pytest is used to check CSV processing, validation errors, and API failure handling. API tests use mocked responses to avoid external network dependencies.