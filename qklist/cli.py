from pathlib import Path
from typing import List, Optional

import typer

from qklist import (
        ERRORS, __app_name__, __version__, config, database, qklist
        )

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
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
            )
        ) -> None:
    return
