import logging

import requests


logger = logging.getLogger(__name__)


def fetch_api_data(url, timeout=5):
    """Fetch JSON data from an API safely."""

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, (dict, list)):
            raise ValueError("API response must be a JSON object or list")

        logger.info("API request successful")
        return data

    except requests.Timeout as error:
        logger.error("API request timed out")
        raise RuntimeError("API request timed out") from error

    except requests.RequestException as error:
        logger.error("API request failed")
        raise RuntimeError("API request failed") from error

    except ValueError as error:
        logger.error("API returned invalid JSON data")
        raise RuntimeError("Invalid API response") from error