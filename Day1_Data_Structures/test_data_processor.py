import pytest
from data_processor import get_unique_ids


def test_removes_duplicate_ids():
    records = [
        {"id": 101},
        {"id": 102},
        {"id": 101},
        {"id": 103},
    ]

    assert get_unique_ids(records) == [101, 102, 103]


def test_empty_records():
    assert get_unique_ids([]) == []


def test_preserves_original_order():
    records = [
        {"id": 30},
        {"id": 10},
        {"id": 20},
    ]

    assert get_unique_ids(records) == [30, 10, 20]
    import pytest


def test_missing_id_raises_error():
    records = [{"name": "API record"}]

    with pytest.raises(KeyError):
         get_unique_ids(records)