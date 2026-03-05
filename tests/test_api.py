"""Tests for teafyi.api — API client initialization and URL construction."""

from teafyi.api import TeaFYI


class TestTeaFYIInit:
    def test_default_base_url(self) -> None:
        client = TeaFYI()
        assert str(client._client.base_url) == "https://teafyi.com"
        client.close()

    def test_custom_base_url(self) -> None:
        client = TeaFYI(base_url="https://custom.example.com")
        assert str(client._client.base_url) == "https://custom.example.com"
        client.close()

    def test_default_timeout(self) -> None:
        client = TeaFYI()
        assert client._client.timeout.connect == 10.0
        client.close()

    def test_custom_timeout(self) -> None:
        client = TeaFYI(timeout=30.0)
        assert client._client.timeout.connect == 30.0
        client.close()

    def test_context_manager(self) -> None:
        with TeaFYI() as api:
            assert str(api._client.base_url) == "https://teafyi.com"


class TestTeaFYIURLConstruction:
    def test_search_url_path(self) -> None:
        """Verify search method would call the correct path (without making HTTP requests)."""
        client = TeaFYI()
        # Build the request manually to verify URL construction
        request = client._client.build_request("GET", "/api/search/", params={"q": "matcha"})
        assert "/api/search/" in str(request.url)
        assert "q=matcha" in str(request.url)
        client.close()
