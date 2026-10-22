import json
from pathlib import Path


def save_report(report, output_path):
    """Save the processing report as a JSON file."""
    path = Path(output_path)

    try:
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding="utf-8") as file:
            json.dump(report, file, indent=4, ensure_ascii=False)

        return {
            "success": True,
            "path": str(path),
            "error": None,
        }

    except OSError as error:
        return {
            "success": False,
            "path": str(path),
            "error": f"Could not save report: {error}",
        }