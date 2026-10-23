# Day 2 - Modular Design and Input Validation

## Objective
Separate JSON parsing and input validation into reusable Python modules.

## Project Structure
- main.py - Runs the application and displays messages.
- parser.py - Parses JSON input and handles malformed JSON.
- validator.py - Validates required book fields and data types.
- test_validator.py - Contains automated tests.

## How to Run
Run the application:

bash
python main.py


Run automated tests:

bash
python -m pytest -v


## Validation Rules
- Input must be a JSON object.
- The id field is required and must be an integer.
- The name field is required and must be a non-empty string.
- Malformed JSON and invalid fields are rejected with useful error messages.

## Test Evidence
Five tests passed:
- Valid book input
- Missing ID
- Missing name
- Malformed JSON
- Empty book name

## Design Decisions
JSON parsing and input validation are separated into different modules to improve readability, reuse, and testing.

## Limitations
This version validates one book at a time and does not store books permanently.