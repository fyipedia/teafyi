---
name: tea-tools
description: Search 200+ tea varieties across 6 categories (white, green, oolong, black, dark, herbal) with chemistry, brewing guides, and origin data.
---

# Tea Tools

Tea variety search and reference powered by [teafyi](https://teafyi.com/) -- a comprehensive tea knowledge platform covering 200+ varieties across 6 oxidation-based categories.

## Setup

Install the MCP server:

```bash
pip install "teafyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "teafyi": {
            "command": "python",
            "args": ["-m", "teafyi.mcp_server"]
        }
    }
}
```

## Available Tools

| Tool | Description |
|------|-------------|
| `tea_search` | Search tea varieties, categories, regions, processing methods, and terminology |

## When to Use

- Looking up tea varieties and their flavor profiles
- Researching tea categories by oxidation level (white → green → oolong → black → dark)
- Finding optimal brewing parameters (temperature, time, leaf-to-water ratio)
- Exploring tea chemistry (L-theanine, catechins, caffeine, theaflavins)
- Learning about tea origins and terroir (Darjeeling, Wuyi, Uji, Assam, etc.)

## Links

- [200+ Tea Varieties](https://teafyi.com/teas/)
- [6 Tea Categories](https://teafyi.com/categories/)
- [Tea Regions](https://teafyi.com/regions/)
- [API Documentation](https://teafyi.com/developers/)
- [PyPI Package](https://pypi.org/project/teafyi/)
