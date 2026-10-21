import time

import requests


class APIClientError(Exception):
    """Raised when an API request fails."""


class APIClient:
    def __init__(self, timeout=5, retries=2, max_pages=3):
        self.timeout = timeout
        self.retries = retries
        self.max_pages = max_pages

    def get(self, url):
        for attempt in range(self.retries + 1):
            try:
                response = requests.get(url, timeout=self.timeout)

                if response.status_code in (429, 500, 502, 503, 504):
                    if attempt < self.retries:
                        time.sleep(0.2 * (attempt + 1))
                        continue

                response.raise_for_status()
                return response

            except (requests.Timeout, requests.ConnectionError) as error:
                if attempt == self.retries:
                    raise APIClientError(
                        "API request failed after retries"
                    ) from error

                time.sleep(0.2 * (attempt + 1))

        raise APIClientError("API request failed")

    def get_json(self, url):
        response = self.get(url)

        try:
            return response.json()
        except ValueError as error:
            raise APIClientError("Invalid JSON response") from error

    def get_pages(self, url):
        results = []

        for page in range(1, self.max_pages + 1):
            data = self.get_json(f"{url}?page={page}")

            if not isinstance(data, list):
                raise APIClientError(
                    "Expected a JSON list for each page"
                )

            results.extend(data)

            if not data:
                break

        return results