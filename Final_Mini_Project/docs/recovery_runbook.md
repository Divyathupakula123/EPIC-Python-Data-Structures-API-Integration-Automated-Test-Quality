# Recovery Runbook

## 1. Missing Input CSV File

*Error:* FileNotFoundError

*Cause:* The input CSV file does not exist at the specified path.

*Recovery:*
1. Check whether data/input.csv exists.
2. Verify the file path passed with --input.
3. Run the application again.

## 2. Invalid CSV Columns

*Error:* ValueError

*Cause:* Required columns are missing.

*Recovery:*
1. Open the input CSV file.
2. Ensure the header contains id, name, and amount.
3. Save the file and run the application again.

## 3. Rejected Records

*Possible reasons:* Empty values, duplicate IDs, or negative amounts.

*Recovery:*
1. Check the rejected records in reports/summary.json.
2. Correct the invalid values in the input CSV.
3. Run the application again.

## 4. API Timeout or Request Failure

*Error:* RuntimeError

*Cause:* The API is slow, unavailable, or the connection failed.

*Recovery:*
1. Verify the API URL.
2. Check the network connection and API availability.
3. Retry when the service is available.
4. Check reports/application.log for error details.

## 5. Tests Fail

*Recovery:*
1. Activate the project virtual environment.
2. Install dependencies using python -m pip install -r requirements.txt.
3. Run python -m pytest tests -v.
4. Review the failed test and fix the underlying issue.

## 6. Restart Procedure

1. Open a terminal in the project root.
2. Activate the virtual environment if required.
3. Run python .\src\main.py.
4. Check the generated files in reports/.

## Important Notes

- API calls are optional.
- Current API tests use mocked responses.
- Automatic retries and restart recovery are not implemented.
- Never store API keys or passwords in source code.