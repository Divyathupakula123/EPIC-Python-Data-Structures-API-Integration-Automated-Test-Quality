def validate_book(data):
    """Validate the required book fields."""

    if not isinstance(data, dict):
        raise ValueError("Input must be a JSON object.")

    if "id" not in data:
        raise ValueError("Missing required field: id.")

    if "name" not in data:
        raise ValueError("Missing required field: name.")

    if not isinstance(data["id"], int) or isinstance(data["id"], bool):
        raise ValueError("Book id must be an integer.")

    if not isinstance(data["name"], str) or not data["name"].strip():
        raise ValueError("Book name must be a non-empty string.")

    return True