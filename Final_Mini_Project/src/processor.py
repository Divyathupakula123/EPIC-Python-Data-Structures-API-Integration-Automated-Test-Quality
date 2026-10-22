import csv
from pathlib import Path


REQUIRED_FIELDS = {"id", "name", "amount"}


def process_csv(input_file, output_file):
    """Validate CSV records and save valid records."""

    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {input_path}"
        )

    valid_records = []
    rejected_records = []

    with input_path.open(
        "r", newline="", encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or not REQUIRED_FIELDS.issubset(
            reader.fieldnames
        ):
            raise ValueError(
                "CSV must contain id, name, amount columns"
            )

        seen_ids = set()

        for row_number, row in enumerate(reader, start=2):
            record_id = (row.get("id") or "").strip()
            name = (row.get("name") or "").strip()
            amount_text = (row.get("amount") or "").strip()

            try:
                if not record_id or not name or not amount_text:
                    raise ValueError("Missing required value")

                if record_id in seen_ids:
                    raise ValueError("Duplicate ID")

                amount = float(amount_text)

                if amount < 0:
                    raise ValueError("Amount cannot be negative")

                seen_ids.add(record_id)

                valid_records.append({
                    "id": record_id,
                    "name": name,
                    "amount": amount,
                })

            except ValueError as error:
                rejected_records.append({
                    "row": row_number,
                    "reason": str(error),
                })

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "name", "amount"],
        )
        writer.writeheader()
        writer.writerows(valid_records)

    return {
        "processed": len(valid_records) + len(rejected_records),
        "valid": len(valid_records),
        "rejected": rejected_records,
        "output_file": str(output_path),
    }