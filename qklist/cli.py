from pathlib import Path
from typing import List, Optional

import typer

from qklist import (ERRORS, __app_name__, __version__, config, database, qklist)

app = typer.Typer()

@app.command()
def init(
        db_path: str = typer.Option(
            str(database.DEFAULT_DB_FILE_PATH),
            "--db-path",
            "-db",
            prompt="Enter qklist database location. Type a path or press enter to confirm default",
            ),
        ) -> None:
    """Initializes the setup for quick list items"""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
                f'Creating qklist configuration file failed with "{ERRORS[app_init_error]}"',
                fg=typer.colors.RED,
                )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
                f'Creating qklist database failed with "{ERRORS[db_init_error]}"',
                fg=typer.colors.RED,
                )
        raise typer.Exit(1)
    else:
        typer.secho(f"Tbe database for qklist saved as [{db_path}]", fg=typer.colors.GREEN)


def get_qklist() -> qklist.QkListObj:
    if config.CONFIG_FILE_PATH.exists():
        db_path = database.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho(
                'Config file not found. Please, run "qklist init"',
                fg=typer.colors.RED,
                )
        raise typer.Exit(1)
    if db_path.exists():
        return qklist.QkListObj(db_path)
    else:
        typer.secho(
                'Database not found. Please, run "qklist init"',
                fg=typer.colors.RED,
                )
        raise typer.Exit(1)


@app.command()
def add(
        description: List[str] = typer.Argument(...),
        priority: int = typer.Option(2, "--priority", "-p", min=1, max=3),
        ) -> None:
    """Add a new item with a DESCRIPTION."""
    current_qklist = get_qklist()
    qklist_item, error = current_qklist.add(description, priority)
    if error:
        typer.secho(
                f'Adding item failed with "{ERRORS[error]}"', fg=typer.colors.RED
                )
        raise typer.Exit(1)
    else:
        typer.secho(
                f"""item: "{qklist_item['Description']}" was added """
                f"""with priority: {priority}""",
                fg=typer.colors.GREEN,
                )


@app.command(name="list")
def list_all() -> None:
    """Show all list items."""
    current_qklist = get_qklist()
    qklist_items = current_qklist.get_qklist_items()
    if len(qklist_items) == 0:
        typer.secho(
                "There are no items in quick list", fg=typer.colors.RED
                )
        raise typer.Exit()
    typer.secho("\nitem list:\n", fg=typer.colors.BLUE, bold=True)
    columns = (
            "ID.  ",
            "| Priority  ",
            "| Done  ",
            "| Description  ",
            )
    headers = "".join(columns)
    typer.secho(headers, fg=typer.colors.BLUE, bold=True)
    typer.secho("-" * len(headers), fg=typer.colors.BLUE)
    for id, list_item in enumerate(qklist_items, 1):
        desc, priority, done = list_item.values()
        typer.secho(
                f"{id}{(len(columns[0]) - len(str(id))) * ' '}"
                f"| ({priority}){(len(columns[1]) - len(str(priority)) - 4) * ' '}"
                f"| {done}{(len(columns[2]) - len(str(done)) - 2) * ' '}"
                f"| {desc}",
                fg=typer.colors.BLUE,
                )
    typer.secho("-" * len(headers) + "\n", fg=typer.colors.BLUE)


@app.command(name="mark")
def set_done(qklist_id: int = typer.Argument(...)) -> None:
    """Mark a list item as done by its id number."""
    current_qklist = get_qklist()
    qklist_item, error = current_qklist.set_done(qklist_id)
    if error:
        typer.secho(
                f'Completing list item # "{qklist_id}" failed with "{ERRORS[error]}"',
                fg=typer.colors.RED,
                )
        raise typer.Exit(1)
    else:
        typer.secho(
                f"""list item # {qklist_id} "{qklist_item['Description']}" completed!""",
                fg=typer.colors.GREEN,
                )


@app.command(name="pull")
def remove(
        listitem_id: int = typer.Argument(...),
        force: bool = typer.Option(
            False,
            "--force",
            "-f",
            help="Force deletion without confirmation.",
            ),
        ) -> None:
    """Remove a list item using its id number."""
    current_qklist = get_qklist()

    def _remove():
        qklist_item, error = current_qklist.remove(listitem_id)
        if error:
            typer.secho(
                    f'Removing list item # {listitem_id} failed with "{ERRORS[error]}"',
                    fg=typer.colors.RED,
                    )
            raise typer.Exit(1)
        else:
            typer.secho(
                    f"""list item # {listitem_id}: '{qklist_item["Description"]}' was removed""",
                    fg=typer.colors.GREEN,
                    )

    if force:
        _remove()
    else:
        qk_list = current_qklist.get_qklist_items()
        try:
            qklist_item = qk_list[listitem_id - 1]
        except IndexError:
            typer.secho("Invalid id number", fg=typer.colors.RED)
            raise typer.Exit(1)
        delete = typer.confirm(
                f"Delete list item # {listitem_id}: {qklist_item['Description']}?"
                )
        if delete:
            _remove()
        else:
            typer.echo("Operation canceled")


@app.command(name="empty")
def remove_all(
        force: bool = typer.Option(
            ...,
            prompt="Delete all list items?",
            help="Force deletion without confirmation.",
            ),
        ) -> None:
    """Empty the list by removing all items."""
    current_qklist = get_qklist()
    if force:
        error = current_qklist.remove_all().error
        if error:
            typer.secho(
                    f'Removing list items failed with "{ERRORS[error]}"',
                    fg=typer.colors.RED,
                    )
            raise typer.Exit(1)
        else:
            typer.secho("All list items were removed", fg=typer.colors.GREEN)
    else:
        typer.echo("Operation canceled")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the version of the application and exit.",
            callback=_version_callback,
            is_eager=True,
            )
        ) -> None:
    return
