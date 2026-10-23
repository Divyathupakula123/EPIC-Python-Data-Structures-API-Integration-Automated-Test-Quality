from collections import deque


def compare_data_structures(records):
    record_list = list(records)

    record_dict = {record["id"]: record for record in records}
    unique_ids = {record["id"] for record in records}

    record_queue = deque(records)
    processed_count = 0

    while record_queue:
        record_queue.popleft()
        processed_count += 1

    return {
        "total_records": len(record_list),
        "unique_records": len(record_dict),
        "unique_ids": len(unique_ids),
        "queue_processed": processed_count,
    }


if __name__ == "__main__":
    records = [
        {"id": 101, "name": "Python"},
        {"id": 102, "name": "Testing"},
        {"id": 101, "name": "Python"},
    ]

    result = compare_data_structures(records)

    print("Data Structure Comparison")
    print("-------------------------")
    print(f"Total records (List): {result['total_records']}")
    print(f"Unique records (Dictionary): {result['unique_records']}")
    print(f"Unique IDs (Set): {result['unique_ids']}")
    print(f"Records processed (Queue): {result['queue_processed']}")