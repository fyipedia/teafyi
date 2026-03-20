"""HTTP API client for teafyi.com REST endpoints.

Requires the ``api`` extra: ``pip install teafyi[api]``

Usage::

    from teafyi.api import TeaFYI

    with TeaFYI() as api:
        items = api.list_benefits()
        detail = api.get_benefit("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class TeaFYI:
    """API client for the teafyi.com REST API.

    Provides typed access to all teafyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://teafyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://teafyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_benefits(self, **params: Any) -> dict[str, Any]:
        """List all benefits."""
        return self._get("/api/v1/benefits/", **params)

    def get_benefit(self, slug: str) -> dict[str, Any]:
        """Get benefit by slug."""
        return self._get(f"/api/v1/benefits/" + slug + "/")

    def list_brewing(self, **params: Any) -> dict[str, Any]:
        """List all brewing."""
        return self._get("/api/v1/brewing/", **params)

    def get_brewing(self, slug: str) -> dict[str, Any]:
        """Get brewing by slug."""
        return self._get(f"/api/v1/brewing/" + slug + "/")

    def list_categories(self, **params: Any) -> dict[str, Any]:
        """List all categories."""
        return self._get("/api/v1/categories/", **params)

    def get_category(self, slug: str) -> dict[str, Any]:
        """Get category by slug."""
        return self._get(f"/api/v1/categories/" + slug + "/")

    def list_compounds(self, **params: Any) -> dict[str, Any]:
        """List all compounds."""
        return self._get("/api/v1/compounds/", **params)

    def get_compound(self, slug: str) -> dict[str, Any]:
        """Get compound by slug."""
        return self._get(f"/api/v1/compounds/" + slug + "/")

    def list_countries(self, **params: Any) -> dict[str, Any]:
        """List all countries."""
        return self._get("/api/v1/countries/", **params)

    def get_country(self, slug: str) -> dict[str, Any]:
        """Get country by slug."""
        return self._get(f"/api/v1/countries/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_processing(self, **params: Any) -> dict[str, Any]:
        """List all processing."""
        return self._get("/api/v1/processing/", **params)

    def get_processing(self, slug: str) -> dict[str, Any]:
        """Get processing by slug."""
        return self._get(f"/api/v1/processing/" + slug + "/")

    def list_regions(self, **params: Any) -> dict[str, Any]:
        """List all regions."""
        return self._get("/api/v1/regions/", **params)

    def get_region(self, slug: str) -> dict[str, Any]:
        """Get region by slug."""
        return self._get(f"/api/v1/regions/" + slug + "/")

    def list_teaware(self, **params: Any) -> dict[str, Any]:
        """List all teaware."""
        return self._get("/api/v1/teaware/", **params)

    def get_teaware(self, slug: str) -> dict[str, Any]:
        """Get teaware by slug."""
        return self._get(f"/api/v1/teaware/" + slug + "/")

    def list_tools(self, **params: Any) -> dict[str, Any]:
        """List all tools."""
        return self._get("/api/v1/tools/", **params)

    def get_tool(self, slug: str) -> dict[str, Any]:
        """Get tool by slug."""
        return self._get(f"/api/v1/tools/" + slug + "/")

    def list_varieties(self, **params: Any) -> dict[str, Any]:
        """List all varieties."""
        return self._get("/api/v1/varieties/", **params)

    def get_variety(self, slug: str) -> dict[str, Any]:
        """Get variety by slug."""
        return self._get(f"/api/v1/varieties/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> TeaFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
