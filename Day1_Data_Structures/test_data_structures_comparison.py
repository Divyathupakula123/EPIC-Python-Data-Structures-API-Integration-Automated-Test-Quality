from data_structures_comparison import compare_data_structures


def test_compares_all_data_structures():
    records = [
        {"id": 101, "name": "Python"},
        {"id": 102, "name": "Testing"},
        {"id": 101, "name": "Python"},
    ]

    result = compare_data_structures(records)

    assert result["total_records"] == 3
    assert result["unique_records"] == 2
    assert result["unique_ids"] == 2
    assert result["queue_processed"] == 3


def test_empty_records():
    result = compare_data_structures([])

    assert result["total_records"] == 0
    assert result["unique_records"] == 0
    assert result["unique_ids"] == 0
    assert result["queue_processed"] == 0