"""Command-line interface for teafyi.

Requires the ``cli`` extra: ``pip install teafyi[cli]``

Usage::

    teafyi search "matcha"
    teafyi search "oolong"
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="teafyi",
    help="Tea knowledge API client — search tea varieties, processing methods, and terms.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def search(
    query: str = typer.Argument(help="Search term (e.g. 'matcha', 'oolong', 'gongfu')"),
) -> None:
    """Search teas, varieties, and glossary terms from TeaFYI."""
    from teafyi.api import TeaFYI

    with TeaFYI() as api:
        data = api.search(query)

    results = data.get("results", [])
    if not results:
        console.print(f"[yellow]No results found for '{query}'[/yellow]")
        return

    table = Table(title=f"Search: {query}")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Name", style="bold")
    table.add_column("URL")

    for item in results:
        table.add_row(
            item.get("type", ""),
            item.get("name", ""),
            item.get("url", ""),
        )

    console.print(table)


if __name__ == "__main__":
    app()
