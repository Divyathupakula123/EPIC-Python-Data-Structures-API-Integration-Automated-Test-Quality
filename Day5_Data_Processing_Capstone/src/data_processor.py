def process_records(records):
    """Validate and process a collection of records."""
    valid_records = []
    rejected_records = []

    for record in records:
        if not isinstance(record, dict):
            rejected_records.append({
                "record": record,
                "reason": "Record must be a dictionary",
            })
            continue

        title = record.get("title")
        user_id = record.get("userId")

        if not isinstance(title, str) or not title.strip():
            rejected_records.append({
                "record": record,
                "reason": "Title is missing or invalid",
            })
            continue

        if not isinstance(user_id, int) or isinstance(user_id, bool) or user_id <= 0:
            rejected_records.append({
                "record": record,
                "reason": "userId must be a positive integer",
            })
            continue

        valid_records.append({
            "userId": user_id,
            "title": title.strip(),
        })

    return {
        "total": len(records),
        "processed": len(valid_records),
        "rejected": len(rejected_records),
        "records": valid_records,
        "errors": rejected_records,
    }