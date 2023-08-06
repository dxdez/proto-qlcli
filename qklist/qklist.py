from pathlib import Path
from typing import Any, Dict, List, NamedTuple

from qklist import DB_READ_ERROR
from qklist.database import DatabaseHandler

class CurrentListItem(NamedTuple):
    listItem: Dict[str, Any]
    error: int

class QkListObj:
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DatabaseHandler(db_path)

    def add(self, description: List[str], priority: int = 2) -> CurrentListItem:
        """Add a new to-do to the database."""
        description_text = " ".join(description)
        if not description_text.endswith("."):
            description_text += "."
        qklistitem = {
            "Description": description_text,
            "Priority": priority,
            "Done": False,
        }
        read = self._db_handler.read_qklists()
        if read.error == DB_READ_ERROR:
            return CurrentListItem(qklistitem, read.error)
        read.qk_list.append(qklistitem)
        write = self._db_handler.write_qklists(read.qk_list)
        return CurrentListItem(qklistitem, write.error)

    def get_qklist_items(self) -> List[Dict[str, Any]]:
        """Return the current to-do list."""
        read = self._db_handler.read_qklists()
        return read.qk_list
