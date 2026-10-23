import json


def parse_json(input_data):
    """Convert a JSON string into Python data."""
    try:
        return json.loads(input_data)
    except json.JSONDecodeError as error:
        raise ValueError("Invalid JSON format.") from error