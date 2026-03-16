# teafyi

[![PyPI version](https://agentgif.com/badge/pypi/teafyi/version.svg)](https://pypi.org/project/teafyi/)
[![Python](https://img.shields.io/pypi/pyversions/teafyi)](https://pypi.org/project/teafyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Tea knowledge API client for Python. Search 60 tea varieties, 15 origin countries, 15 teaware items, and tea terminology from [TeaFYI](https://teafyi.com) -- the comprehensive tea reference with 120 expert guides covering oxidation science, processing methods, brewing parameters, and the world's tea traditions.

> **Explore tea at [teafyi.com](https://teafyi.com)** -- [Tea Varieties](https://teafyi.com/teas/) | [Origins](https://teafyi.com/origins/) | [Teaware](https://teafyi.com/teaware/) | [Tea Guides](https://teafyi.com/guides/)

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/teafyi/main/demo.gif" alt="teafyi demo -- tea variety API search and lookup" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You'll Find on TeaFYI](#what-youll-find-on-teafyi)
  - [Tea Categories by Oxidation](#tea-categories-by-oxidation)
  - [Processing Methods](#processing-methods)
  - [Teaware](#teaware)
  - [Key Tea Concepts](#key-tea-concepts)
- [API Endpoints](#api-endpoints)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [API Client](#api-client)
- [Learn More About Tea](#learn-more-about-tea)
- [Beverage FYI Family](#beverage-fyi-family)
- [License](#license)

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
    # Search tea varieties, origins, teaware, glossary terms
    results = api.search("matcha")
    print(results)

    # Look up a glossary term
    term = api.glossary_term("oxidation")
    print(term["definition"])
```

## What You'll Find on TeaFYI

TeaFYI is a comprehensive tea reference covering 60 tea varieties, 15 origin countries, 15 teaware items, and 120 expert guides. All true tea comes from a single plant species -- **Camellia sinensis** -- and the vast differences between a delicate white tea and a robust black tea are created entirely through processing, particularly the degree of oxidation.

### Tea Categories by Oxidation

Tea is classified into six major categories based on oxidation level -- the enzymatic browning process that occurs when tea leaves are exposed to oxygen after picking. Oxidation is the single most important factor determining a tea's character:

| Category | Oxidation | Processing | Characteristics |
|----------|-----------|------------|-----------------|
| Green | 0-5% | Kill-green (pan-fired or steamed), rolled, dried | Vegetal, grassy, sweet, bright green liquor |
| White | 0-10% | Minimal processing, withered and dried | Delicate, floral, honey, subtle sweetness |
| Yellow | 5-15% | Kill-green, wrapped/heaped (men huan), dried | Mellow, smooth, less grassy than green |
| Oolong | 15-85% | Withered, bruised, partial oxidation, shaped | Complex range from floral to toasty |
| Black | 85-100% | Withered, rolled, fully oxidized, dried | Malty, robust, tannic, amber-red liquor |
| Pu-erh | Post-fermented | Microbial fermentation (sheng or shou) | Earthy, woody, complex, ages for decades |

Herbal infusions (chamomile, rooibos, peppermint) are technically tisanes, not tea, as they do not come from Camellia sinensis. TeaFYI covers both categories.

Learn more: [Browse Tea Categories](https://teafyi.com/category/) · [Tea Encyclopedia](https://teafyi.com/tea/)

### Processing Methods

Beyond oxidation, specific processing steps create the diversity within each tea category:

| Process | Description | Applied To |
|---------|-------------|------------|
| Kill-Green (Sha Qing) | Heat stops oxidation -- pan-fired or steamed | Green, Yellow |
| Withering | Leaves lose moisture, become pliable | White, Oolong, Black |
| Rolling/Shaping | Breaks cell walls, releases oils, shapes leaf | Green, Oolong, Black |
| CTC (Cut-Tear-Curl) | Machine processing for consistent, strong brew | CTC Black (tea bags) |
| Orthodox | Hand-plucked, gentle processing, whole leaf | Specialty loose leaf |
| Pile Fermentation (Wo Dui) | Accelerated microbial aging in humid conditions | Shou (Ripe) Pu-erh |

The distinction between CTC and orthodox processing is fundamental: CTC produces small, uniform granules that brew quickly and strongly (ideal for tea bags and chai), while orthodox processing preserves whole leaves with more nuanced, complex flavor (ideal for gongfu brewing).

Learn more: [Processing Methods](https://teafyi.com/processing/) · [Tea Glossary](https://teafyi.com/glossary/)

### Teaware

TeaFYI catalogs 15 teaware items with materials, origins, and recommended uses. The brewing vessel profoundly affects tea character -- porous Yixing clay absorbs tea oils over time, while glass and porcelain offer neutral, clean extraction:

| Teaware | Material | Origin | Best For |
|---------|----------|--------|----------|
| Gaiwan | Porcelain | China | Universal, gongfu brewing |
| Yixing Teapot | Zisha clay | Yixing, China | Oolong, Pu-erh, dedicated to one tea type |
| Kyusu | Ceramic | Japan | Japanese green tea (sencha, gyokuro) |
| Tetsubin | Cast iron | Japan | Boiling water, heat retention |
| Glass Teapot | Borosilicate | Modern | Flowering tea, visual appreciation |
| Chasen | Bamboo whisk | Japan | Matcha preparation |

Learn more: [Teaware Guide](https://teafyi.com/teaware/) · [Brewing Guides](https://teafyi.com/guide/)

### Key Tea Concepts

| Concept | Description |
|---------|-------------|
| First Flush | First spring harvest, prized for freshness and delicacy (Darjeeling, Shincha) |
| Second Flush | Summer harvest, fuller body and muscatel character |
| Terroir | Altitude, soil, climate, and fog patterns that create regional character |
| Gongfu Cha | Chinese brewing method: small vessel, high leaf ratio, multiple short infusions |
| Caffeine Content | Varies by processing: matcha highest (~70mg/cup), white tea lowest (~15-30mg/cup) |
| L-Theanine | Amino acid unique to tea, promotes calm alertness, highest in shade-grown teas |

Learn more: [Tea Science](https://teafyi.com/science/) · [Tea Compounds](https://teafyi.com/compound/)

## API Endpoints

All endpoints are free, require no authentication, and return JSON with CORS enabled.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/teas/` | List all 60 tea varieties |
| GET | `/api/v1/teas/{slug}/` | Tea variety detail with brewing params |
| GET | `/api/v1/origins/` | List all 15 origin countries |
| GET | `/api/v1/origins/{slug}/` | Origin detail with regions, climate |
| GET | `/api/v1/teaware/` | List all 15 teaware items |
| GET | `/api/v1/teaware/{slug}/` | Teaware detail with materials, use |
| GET | `/api/v1/glossary/` | List all tea terminology |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two tea varieties |
| GET | `/api/v1/random/` | Random tea variety |
| GET | `/api/v1/guides/` | List all 120 guides |
| GET | `/api/v1/guides/{slug}/` | Guide detail |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

### Example

```bash
curl -s "https://teafyi.com/api/v1/teas/matcha/"
```

```json
{
  "slug": "matcha",
  "name": "Matcha",
  "category": "Green",
  "description": "Stone-ground Japanese green tea powder made from shade-grown tencha leaves, whisked with hot water for a rich, umami-forward brew.",
  "origin": "Japan",
  "oxidation": "0%",
  "caffeine": "high",
  "flavor_profile": ["umami", "vegetal", "sweet", "creamy"],
  "brewing": {
    "temperature": "70-80C",
    "amount": "2g per 60ml",
    "method": "Whisk with chasen until frothy"
  },
  "url": "https://teafyi.com/teas/matcha/"
}
```

Full API documentation: [teafyi.com/developers/](https://teafyi.com/developers/).
OpenAPI 3.1.0 spec: [teafyi.com/api/v1/openapi.json](https://teafyi.com/api/v1/openapi.json).

## Command-Line Interface

```bash
# Search tea varieties, origins, teaware
teafyi search "matcha"
teafyi search "oolong"
teafyi search "gongfu ceremony"
teafyi search "darjeeling"

# Look up tea terminology
teafyi term "oxidation"
teafyi term "first-flush"
teafyi term "gaiwan"
```

The CLI displays results in formatted tables with rich terminal output.

## MCP Server (Claude, Cursor, Windsurf)

Run as an MCP server for AI-assisted tea queries:

```bash
python -m teafyi.mcp_server
```

**Claude Desktop** (`~/.claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "teafyi": {
      "command": "uvx",
      "args": ["--from", "teafyi[mcp]", "python", "-m", "teafyi.mcp_server"]
    }
  }
}
```

**Tools**: `tea_search`, `tea_glossary_term`

## API Client

```python
from teafyi.api import TeaFYI

with TeaFYI() as api:
    # Search across teas, origins, teaware, glossary
    results = api.search("oolong")

    # Look up tea terminology
    term = api.glossary_term("gongfu")
    print(term["definition"])

    # Compare two tea varieties
    comparison = api.compare("sencha", "matcha")

    # Get a random tea variety
    random_tea = api.random()
```

## Learn More About Tea

- **Reference**: [Tea Varieties](https://teafyi.com/teas/) | [Origins](https://teafyi.com/origins/) | [Teaware](https://teafyi.com/teaware/)
- **Glossary**: [Tea Terminology](https://teafyi.com/glossary/)
- **Guides**: [Tea Guides](https://teafyi.com/guides/)
- **Compare**: [Tea Comparisons](https://teafyi.com/compare/)
- **API**: [Developer Docs](https://teafyi.com/developers/) | [OpenAPI Spec](https://teafyi.com/api/v1/openapi.json)

## Beverage FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem -- world beverages from cocktails to sake.

| Site | Domain | Focus |
|------|--------|-------|
| CocktailFYI | [cocktailfyi.com](https://cocktailfyi.com) | 636 cocktails, ABV, calories, flavor profiles |
| VinoFYI | [vinofyi.com](https://vinofyi.com) | Wines, grapes, regions, wineries, food pairings |
| BeerFYI | [beerfyi.com](https://beerfyi.com) | 112 beer styles, hops, malts, yeast, BJCP |
| BrewFYI | [brewfyi.com](https://brewfyi.com) | 72 coffee varieties, roasting, 21 brew methods |
| WhiskeyFYI | [whiskeyfyi.com](https://whiskeyfyi.com) | 80 whiskey expressions, distilleries, regions |
| **TeaFYI** | [teafyi.com](https://teafyi.com) | **60 tea varieties, teaware, brewing guides** |
| NihonshuFYI | [nihonshufyi.com](https://nihonshufyi.com) | 80 sake, rice varieties, 50 breweries |

## License

MIT
