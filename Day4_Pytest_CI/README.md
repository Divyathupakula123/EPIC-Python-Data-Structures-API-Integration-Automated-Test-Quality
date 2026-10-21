# Day 4 - Pytest, Fixtures and CI

*Date:* Thursday, 22 October 2026

## Objective
To improve automated testing using pytest fixtures, parametrized tests, boundary cases, and Continuous Integration (CI).

## Tasks Completed
- Created automated tests using pytest.
- Added a reusable pytest fixture.
- Added parametrized tests for multiple input combinations.
- Tested zero, negative, and large integer values.
- Configured GitHub Actions to run tests automatically.
- Ensured tests do not require a live external service.

## Project Files
- test_pytest_ci.py - Test functions and test cases.
- .github/workflows/tests.yml - GitHub Actions CI workflow.
- README.md - Project documentation.

## Technologies Used
- Python 3.12
- pytest
- GitHub Actions
- VS Code

## How to Run the Tests
Run the following command from the project folder:

powershell
python -m pytest -v


## Test Coverage
- Normal addition
- Zero boundary case
- Negative numbers
- Large integer values
- Reusable fixture
- Parametrized test cases

## Test Evidence
*Result:* 27 tests passed.

All tests run locally without accessing a live external service.

## CI Workflow
GitHub Actions runs the pytest suite when code is pushed or a pull request is opened.

## Known Limitations
- The project currently tests a simple addition function.
- Code coverage percentage has not been measured.
- GitHub Actions execution must be verified in the GitHub repository.

## Conclusion
The Day 4 task demonstrates pytest fixtures, parametrized tests, boundary testing, and automated CI configuration.