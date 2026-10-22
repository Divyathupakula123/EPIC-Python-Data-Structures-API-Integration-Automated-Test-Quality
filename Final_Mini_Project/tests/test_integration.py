import json

from src.main import main


def test_complete_workflow(tmp_path, monkeypatch):
    input_file = tmp_path / "input.csv"
    input_file.write_text(
        "id,name,amount\n"
        "101,Divya,1500\n"
        "102,Ravi,2500\n"
        "102,Kiran,1800\n",
        encoding="utf-8",
    )

    reports_dir = tmp_path / "reports"
    reports_dir.mkdir()

    monkeypatch.setattr(
        "src.main.REPORTS_DIR", reports_dir
    )
    monkeypatch.setattr(
        "src.main.fetch_api_data",
        lambda url: {"status": "success"},
    )
    monkeypatch.setattr(
        "sys.argv",
        [
            "main.py",
            "--input",
            str(input_file),
            "--api-url",
            "https://example.com/api",
        ],
    )

    main()

    summary = json.loads(
        (reports_dir / "summary.json").read_text(
            encoding="utf-8"
        )
    )
    api_data = json.loads(
        (reports_dir / "api_response.json").read_text(
            encoding="utf-8"
        )
    )

    assert summary["processed"] == 3
    assert summary["valid"] == 2
    assert len(summary["rejected"]) == 1
    assert summary["rejected"][0]["reason"] == "Duplicate ID"
    assert api_data["status"] == "success"