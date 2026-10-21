# Day 3: API Client and Failure Handling

## Objective
Build a reliable Python API client with timeouts, limited retries,
HTTP status validation, JSON validation, and bounded pagination.

## Technologies
- Python
- Requests
- Pytest
- unittest.mock

## Features
- Configurable request timeout
- Limited retries for timeouts and connection errors
- Retries for selected transient HTTP status codes
- HTTP status validation
- Malformed JSON handling
- Bounded pagination

## Project Files
- api_client.py: API client implementation
- test_api_client.py: Mocked automated tests
- requirements.txt: Project dependencies

## Setup
Create and activate a virtual environment, then run:

    python -m pip install -r requirements.txt

## Run Tests

    python -m pytest -v

## Test Evidence
Five mocked tests passed:
- Successful API request
- Timeout after retries
- HTTP 404 error
- Malformed JSON
- Bounded pagination

## Design Decisions
GET requests are used because they are generally safe to retry.
Retries are limited to avoid endless requests.
Pagination has a configurable maximum page count.

## Known Limitations
- Retry-After is not implemented.
- Pagination assumes the API accepts a page query parameter.
- Authentication and rate-limit policies are not implemented.
- Tests use mocked responses and do not verify a live API.