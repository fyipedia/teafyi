# teafyi

Tea knowledge API client for developers -- search tea varieties, processing methods, and terminology from [TeaFYI](https://teafyi.com).

## Install

```bash
pip install teafyi[api]     # API client (httpx)
pip install teafyi[cli]     # + CLI (typer, rich)
pip install teafyi[mcp]     # + MCP server
pip install teafyi[all]     # Everything
```

## Quick Start

```python
from teafyi.api import TeaFYI

with TeaFYI() as api:
    results = api.search("matcha")
    print(results)
```

## CLI

```bash
teafyi search "matcha"
teafyi search "oolong"
teafyi search "gongfu ceremony"
```

## MCP Server

```bash
# Add to Claude Desktop config
python -m teafyi.mcp_server
```

Tools: `tea_search`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `search(query)` | `GET /api/search/?q=...` | Search teas, varieties, and terms |

## Links

- [TeaFYI](https://teafyi.com) -- Tea encyclopedia with categories, varieties, processing methods, and more
- [PyPI](https://pypi.org/project/teafyi/)
- [GitHub](https://github.com/fyipedia/teafyi)
- [FYIPedia](https://fyipedia.com) -- Open-source developer tools ecosystem
