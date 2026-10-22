import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def fetch_records(url, timeout=5):
    """Fetch JSON records from an API and handle recoverable failures."""
    request = Request(
        url,
        headers={"User-Agent": "Day5-Data-Processing-Capstone"},
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))

        if not isinstance(data, list):
            return {
                "success": False,
                "records": [],
                "error": "API response must be a JSON list",
            }

        return {
            "success": True,
            "records": data,
            "error": None,
        }

    except HTTPError as error:
        return {
            "success": False,
            "records": [],
            "error": f"HTTP error: {error.code}",
        }

    except (URLError, TimeoutError, OSError) as error:
        return {
            "success": False,
            "records": [],
            "error": f"Network error: {error}",
        }

    except (json.JSONDecodeError, UnicodeDecodeError):
        return {
            "success": False,
            "records": [],
            "error": "API returned invalid JSON",
        }