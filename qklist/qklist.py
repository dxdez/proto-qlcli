from pathlib import Path
from typing import Any, Dict, NamedTuple

from qklist.database import DatabaseHandler

class CurrentListItem(NamedTuple):
    listItem: Dict[str, Any]
    error: int

class QkListObj:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)
