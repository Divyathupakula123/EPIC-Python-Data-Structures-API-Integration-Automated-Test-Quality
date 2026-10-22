from pathlib import Path

from src.api_client import fetch_records
from src.data_processor import process_records
from src.report_generator import save_report


API_URL = "https://jsonplaceholder.typicode.com/todos"
OUTPUT_PATH = Path("output/report.json")


def main():
    print("Data Processing Capstone")
    print("-" * 30)

    api_result = fetch_records(API_URL)

    if api_result["success"]:
        records = api_result["records"]
        print(f"API records received: {len(records)}")
    else:
        print(f"API unavailable: {api_result['error']}")
        print("Using sample data instead.")

        records = [
            {"userId": 1, "title": "Learn Python"},
            {"userId": 2, "title": "Build a project"},
            {"userId": 0, "title": "Invalid record"},
            {"userId": 3, "title": ""},
        ]

    report = process_records(records)
    save_result = save_report(report, OUTPUT_PATH)

    print(f"Total records: {report['total']}")
    print(f"Processed: {report['processed']}")
    print(f"Rejected: {report['rejected']}")

    if save_result["success"]:
        print(f"Report saved to: {save_result['path']}")
    else:
        print(save_result["error"])


if __name__ == "__main__":
    main()