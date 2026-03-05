"""MCP server for teafyi — tea knowledge tools for AI assistants.

Requires the ``mcp`` extra: ``pip install teafyi[mcp]``

Run as a standalone server::

    python -m teafyi.mcp_server

Or configure in ``claude_desktop_config.json``::

    {
        "mcpServers": {
            "teafyi": {
                "command": "python",
                "args": ["-m", "teafyi.mcp_server"]
            }
        }
    }
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("teafyi")


@mcp.tool()
def tea_search(query: str) -> str:
    """Search teas, varieties, processing methods, and glossary terms from TeaFYI.

    Covers green tea, black tea, oolong, white tea, pu-erh, matcha, herbal teas,
    tea ceremony traditions, teaware, and more.

    Args:
        query: Search term (e.g. "matcha", "oolong", "gongfu ceremony").
    """
    from teafyi.api import TeaFYI

    with TeaFYI() as api:
        data = api.search(query)

    results = data.get("results", [])
    if not results:
        return f"No results found for '{query}'."

    lines = [
        f"## Tea Search: {query}",
        "",
        f"Found {len(results)} result(s):",
        "",
        "| Type | Name | URL |",
        "|------|------|-----|",
    ]
    for item in results:
        item_type = item.get("type", "")
        name = item.get("name", "")
        url = item.get("url", "")
        lines.append(f"| {item_type} | {name} | {url} |")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
