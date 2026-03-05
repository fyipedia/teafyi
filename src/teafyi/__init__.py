"""teafyi — Tea knowledge API client for developers.

Search tea varieties, processing methods, and terminology from TeaFYI.

Usage::

    from teafyi.api import TeaFYI

    with TeaFYI() as api:
        results = api.search("matcha")
        print(results)
"""

__version__ = "0.1.0"
