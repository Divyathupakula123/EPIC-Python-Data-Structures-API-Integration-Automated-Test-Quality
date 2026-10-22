import argparse
import json
import logging
from pathlib import Path

try:
    from .api_client import fetch_api_data
    from .processor import process_csv
except ImportError:
    from api_client import fetch_api_data
    from processor import process_csv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(REPORTS_DIR / "application.log", encoding="utf-8"),
    ],
)

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Reliable Data Processing Utility"
    )
    parser.add_argument(
        "--input",
        default=str(PROJECT_ROOT / "data" / "input.csv"),
        help="Path to input CSV file",
    )
    parser.add_argument(
        "--api-url",
        default=None,
        help="Optional API URL returning JSON data",
    )
    args = parser.parse_args()



    try:
        result = process_csv(
            args.input,
            REPORTS_DIR / "processed.csv",
        )

        if args.api_url:
            api_data = fetch_api_data(args.api_url)
            with (REPORTS_DIR / "api_response.json").open(
                "w", encoding="utf-8"
            ) as file:
                json.dump(api_data, file, indent=2)

        report_path = REPORTS_DIR / "summary.json"
        with report_path.open("w", encoding="utf-8") as file:
            json.dump(result, file, indent=2)

        logger.info(
            "Processing complete: %s valid, %s rejected",
            result["valid"],
            len(result["rejected"]),
        )
        print(json.dumps(result, indent=2))

    except (OSError, ValueError, RuntimeError) as error:
        logger.error("Workflow failed: %s", error)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()