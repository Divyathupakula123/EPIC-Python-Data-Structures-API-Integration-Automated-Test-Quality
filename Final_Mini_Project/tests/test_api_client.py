import pytest
import requests

from src.api_client import fetch_api_data


def test_api_success(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"status": "success"}

    monkeypatch.setattr(
        "src.api_client.requests.get",
        lambda url, timeout: FakeResponse(),
    )

    result = fetch_api_data("https://example.com/api")

    assert result == {"status": "success"}


def test_api_timeout(monkeypatch):
    def fake_get(url, timeout):
        raise requests.Timeout("Request timed out")

    monkeypatch.setattr(
        "src.api_client.requests.get",
        fake_get,
    )

    with pytest.raises(RuntimeError, match="timed out"):
        fetch_api_data("https://example.com/api")


def test_api_http_failure(monkeypatch):
    def fake_get(url, timeout):
        raise requests.ConnectionError("Connection failed")

    monkeypatch.setattr(
        "src.api_client.requests.get",
        fake_get,
    )

    with pytest.raises(RuntimeError, match="failed"):
        fetch_api_data("https://example.com/api")