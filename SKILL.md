---
name: tea-tools
description: Search 60 tea varieties, 15 origin countries, 15 teaware items, and tea terminology from TeaFYI. Use when answering questions about tea categories, oxidation science, brewing parameters, or teaware.
license: MIT
metadata:
  author: fyipedia
  version: "0.1.1"
  homepage: "https://teafyi.com/"
---

# TeaFYI -- Tea Tools for AI Agents

Tea knowledge API client for Python. Search 60 tea varieties, 15 origin countries, 15 teaware items, and tea terminology from TeaFYI -- the comprehensive tea reference with 120 expert guides covering oxidation science, processing methods, brewing parameters, and the world's tea traditions.

**Install**: `pip install teafyi[api]` -- **Web**: [teafyi.com](https://teafyi.com/) -- **API**: [REST API](https://teafyi.com/developers/) -- **PyPI**: [teafyi](https://pypi.org/project/teafyi/)

## When to Use

- User asks about tea categories, varieties, or oxidation levels
- User needs brewing parameters (temperature, steep time, leaf ratio)
- User wants teaware recommendations (gaiwan, Yixing, kyusu)
- User asks about tea processing (kill-green, withering, CTC vs orthodox)
- User needs tea terminology definitions (gongfu, first flush, L-theanine)

## Tools

### `TeaFYI` API Client

HTTP client for the teafyi.com REST API. Requires `pip install teafyi[api]`.

```python
from teafyi.api import TeaFYI

with TeaFYI() as api:
    results = api.search("matcha")     # Search teas, origins, teaware, glossary
```

**Methods:**
- `search(query: str) -> dict` -- Search teas, varieties, and glossary terms

## REST API (No Auth Required)

```bash
# Search
curl "https://teafyi.com/api/v1/search/?q=matcha"

# Tea variety detail
curl "https://teafyi.com/api/v1/teas/matcha/"

# Teaware detail
curl "https://teafyi.com/api/v1/teaware/gaiwan/"

# Glossary term
curl "https://teafyi.com/api/v1/glossary/oxidation/"

# Compare two teas
curl "https://teafyi.com/api/v1/compare/matcha/sencha/"
```

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/teas/` | List all 60 tea varieties |
| GET | `/api/v1/teas/{slug}/` | Tea variety detail with brewing params |
| GET | `/api/v1/origins/` | List all 15 origin countries |
| GET | `/api/v1/origins/{slug}/` | Origin detail with regions, climate |
| GET | `/api/v1/teaware/` | List all 15 teaware items |
| GET | `/api/v1/teaware/{slug}/` | Teaware detail with materials, use |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two tea varieties |
| GET | `/api/v1/random/` | Random tea variety |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

Full spec: [OpenAPI 3.1.0](https://teafyi.com/api/v1/openapi.json)

## Tea Categories by Oxidation

| Category | Oxidation | Characteristics |
|----------|-----------|-----------------|
| Green | 0-5% | Vegetal, grassy, sweet, bright green liquor |
| White | 0-10% | Delicate, floral, honey, subtle sweetness |
| Yellow | 5-15% | Mellow, smooth, less grassy than green |
| Oolong | 15-85% | Complex range from floral to toasty |
| Black | 85-100% | Malty, robust, tannic, amber-red liquor |
| Pu-erh | Post-fermented | Earthy, woody, complex, ages for decades |

## Processing Methods

| Process | Description | Applied To |
|---------|-------------|------------|
| Kill-Green (Sha Qing) | Heat stops oxidation -- pan-fired or steamed | Green, Yellow |
| Withering | Leaves lose moisture, become pliable | White, Oolong, Black |
| Rolling/Shaping | Breaks cell walls, releases oils | Green, Oolong, Black |
| CTC (Cut-Tear-Curl) | Machine processing, strong brew | CTC Black (tea bags) |
| Orthodox | Hand-plucked, whole leaf | Specialty loose leaf |
| Pile Fermentation | Accelerated microbial aging | Shou (Ripe) Pu-erh |

## Teaware

| Teaware | Material | Best For |
|---------|----------|----------|
| Gaiwan | Porcelain | Universal, gongfu brewing |
| Yixing Teapot | Zisha clay | Oolong, Pu-erh |
| Kyusu | Ceramic | Japanese green tea |
| Tetsubin | Cast iron | Boiling water, heat retention |
| Chasen | Bamboo whisk | Matcha preparation |

## Key Tea Concepts

| Concept | Description |
|---------|-------------|
| Gongfu Cha | Small vessel, high leaf ratio, multiple short infusions |
| First Flush | First spring harvest, prized for freshness and delicacy |
| L-Theanine | Amino acid promoting calm alertness, highest in shade-grown teas |
| Caffeine | Varies: matcha highest (~70mg/cup), white tea lowest (~15-30mg/cup) |

## Demo

![TeaFYI demo](https://raw.githubusercontent.com/fyipedia/teafyi/main/demo.gif)

## Beverage FYI Family

Part of the [FYIPedia](https://fyipedia.com) ecosystem: [CocktailFYI](https://cocktailfyi.com), [VinoFYI](https://vinofyi.com), [BeerFYI](https://beerfyi.com), [BrewFYI](https://brewfyi.com), [WhiskeyFYI](https://whiskeyfyi.com), [TeaFYI](https://teafyi.com), [NihonshuFYI](https://nihonshufyi.com).
