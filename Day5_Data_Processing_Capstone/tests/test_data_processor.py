from src.data_processor import process_records


def test_process_valid_records():
    records = [
        {"userId": 1, "title": "Learn Python"},
        {"userId": 2, "title": "Build a project"},
    ]

    result = process_records(records)

    assert result["total"] == 2
    assert result["processed"] == 2
    assert result["rejected"] == 0


def test_reject_invalid_records():
    records = [
        {"userId": 1, "title": "Valid"},
        {"userId": 0, "title": "Invalid user"},
        {"userId": 2, "title": ""},
    ]

    result = process_records(records)

    assert result["total"] == 3
    assert result["processed"] == 1
    assert result["rejected"] == 2


def test_empty_collection():
    result = process_records([])

    assert result["total"] == 0
    assert result["processed"] == 0
    assert result["rejected"] == 0


def test_non_dictionary_record():
    result = process_records(["invalid"])

    assert result["processed"] == 0
    assert result["rejected"] == 1