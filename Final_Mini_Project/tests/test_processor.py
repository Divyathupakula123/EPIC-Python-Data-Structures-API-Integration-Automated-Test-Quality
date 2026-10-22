import csv

import pytest

from src.processor import process_csv


def test_process_csv_valid_and_invalid_records(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    input_file.write_text(
        "id,name,amount\n"
        "101,Divya,1500\n"
        "102,Ravi,2500\n"
        "102,Kiran,1800\n"
        "103,Sita,-500\n"
        "104,,900\n",
        encoding="utf-8",
    )

    result = process_csv(input_file, output_file)

    assert result["processed"] == 5
    assert result["valid"] == 2
    assert len(result["rejected"]) == 3

    with output_file.open(
        newline="", encoding="utf-8"
    ) as file:
        records = list(csv.DictReader(file))

    assert len(records) == 2
    assert records[0]["name"] == "Divya"


def test_missing_input_file(tmp_path):
    input_file = tmp_path / "missing.csv"
    output_file = tmp_path / "output.csv"

    with pytest.raises(FileNotFoundError):
        process_csv(input_file, output_file)


def test_missing_required_column(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    input_file.write_text(
        "id,name\n101,Divya\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="CSV must contain"):
        process_csv(input_file, output_file)