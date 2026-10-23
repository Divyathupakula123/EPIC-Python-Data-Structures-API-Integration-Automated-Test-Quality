import pytest

from parser import parse_json
from validator import validate_book


def test_valid_book():
    data = parse_json('{"id": 101, "name": "Python Basics"}')
    assert validate_book(data) is True


def test_missing_id_raises_error():
    data = {"name": "Python Basics"}

    with pytest.raises(ValueError, match="Missing required field: id"):
        validate_book(data)


def test_missing_name_raises_error():
    data = {"id": 101}

    with pytest.raises(ValueError, match="Missing required field: name"):
        validate_book(data)


def test_malformed_json_raises_error():
    with pytest.raises(ValueError, match="Invalid JSON format"):
        parse_json('{"id": 101, "name":')


def test_empty_name_raises_error():
    data = {"id": 101, "name": "   "}

    with pytest.raises(ValueError, match="non-empty string"):
        validate_book(data)