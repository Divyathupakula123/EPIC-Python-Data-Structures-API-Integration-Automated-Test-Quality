import pytest
import requests
from unittest.mock import Mock, patch

from api_client import APIClient, APIClientError


@patch("api_client.requests.get")
def test_successful_api_request(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "Python"}]
    mock_get.return_value = mock_response

    client = APIClient()
    result = client.get_json("https://example.com/books")

    assert result == [{"id": 1, "name": "Python"}]
    mock_get.assert_called_once()


@patch("api_client.time.sleep")
@patch("api_client.requests.get")
def test_timeout_raises_error_after_retries(mock_get, mock_sleep):
    mock_get.side_effect = requests.Timeout("Request timed out")

    client = APIClient(retries=2)

    with pytest.raises(APIClientError, match="failed after retries"):
        client.get("https://example.com/books")

    assert mock_get.call_count == 3


@patch("api_client.requests.get")
def test_http_error_status(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.HTTPError("404")
    mock_get.return_value = mock_response

    client = APIClient(retries=0)

    with pytest.raises(requests.HTTPError):
        client.get("https://example.com/books")


@patch("api_client.requests.get")
def test_malformed_json(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_get.return_value = mock_response

    client = APIClient()

    with pytest.raises(APIClientError, match="Invalid JSON"):
        client.get_json("https://example.com/books")


@patch("api_client.requests.get")
def test_pagination_is_bounded(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1}]
    mock_get.return_value = mock_response

    client = APIClient(max_pages=3)
    result = client.get_pages("https://example.com/books")

    assert len(result) == 3
    assert mock_get.call_count == 3