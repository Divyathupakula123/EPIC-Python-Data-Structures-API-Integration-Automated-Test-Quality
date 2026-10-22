from unittest.mock import patch
from urllib.error import URLError

from src.api_client import fetch_records


def test_fetch_records_success():
    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self):
            return b'[{"userId": 1, "title": "Python"}]'

    with patch("src.api_client.urlopen", return_value=FakeResponse()):
        result = fetch_records("https://example.com/test")

    assert result["success"] is True
    assert len(result["records"]) == 1
    assert result["error"] is None


def test_fetch_records_network_failure():
    with patch(
        "src.api_client.urlopen",
        side_effect=URLError("Network unavailable"),
    ):
        result = fetch_records("https://example.com/test")

    assert result["success"] is False
    assert result["records"] == []
    assert "Network error" in result["error"]


def test_fetch_records_invalid_json():
    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self):
            return b"not-json"

    with patch("src.api_client.urlopen", return_value=FakeResponse()):
        result = fetch_records("https://example.com/test")

    assert result["success"] is False
    assert result["error"] == "API returned invalid JSON"