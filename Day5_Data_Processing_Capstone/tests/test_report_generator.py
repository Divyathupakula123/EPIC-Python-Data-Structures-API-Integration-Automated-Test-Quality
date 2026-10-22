import json

from src.report_generator import save_report


def test_save_report_success(tmp_path):
    report = {
        "total": 2,
        "processed": 1,
        "rejected": 1,
        "records": [{"userId": 1, "title": "Python"}],
        "errors": [],
    }

    output_file = tmp_path / "report.json"
    result = save_report(report, output_file)

    assert result["success"] is True
    assert output_file.exists()

    saved_report = json.loads(output_file.read_text(encoding="utf-8"))
    assert saved_report["total"] == 2


def test_save_report_failure(tmp_path):
    from unittest.mock import patch

    with patch(
        "src.report_generator.Path.open",
        side_effect=OSError("Permission denied"),
    ):
        result = save_report({"total": 0}, tmp_path / "report.json")

    assert result["success"] is False
    assert "Could not save report" in result["error"]