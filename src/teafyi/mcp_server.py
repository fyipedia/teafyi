"""MCP server for teafyi — AI assistant tools for teafyi.com.

Run: uvx --from "teafyi[mcp]" python -m teafyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TeaFYI")


@mcp.tool()
def list_categories(limit: int = 20, offset: int = 0) -> str:
    """List categories from teafyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from teafyi.api import TeaFYI

    with TeaFYI() as api:
        data = api.list_categories(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No categories found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_category(slug: str) -> str:
    """Get detailed information about a specific category.

    Args:
        slug: URL slug identifier for the category.
    """
    from teafyi.api import TeaFYI

    with TeaFYI() as api:
        data = api.get_category(slug)
        return str(data)


@mcp.tool()
def list_compounds(limit: int = 20, offset: int = 0) -> str:
    """List compounds from teafyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from teafyi.api import TeaFYI

    with TeaFYI() as api:
        data = api.list_compounds(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No compounds found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_tea(query: str) -> str:
    """Search teafyi.com for tea varieties, brewing methods, and benefits.

    Args:
        query: Search query string.
    """
    from teafyi.api import TeaFYI

    with TeaFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
