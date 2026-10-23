def get_unique_ids(records):
    """Return unique record IDs while preserving their order."""
    seen = set()
    unique_ids = []

    for record in records:
        record_id = record["id"]

        if record_id not in seen:
            seen.add(record_id)
            unique_ids.append(record_id)

    return unique_ids