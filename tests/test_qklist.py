import json
import pytest
from typer.testing import CliRunner

from qklist import (
    DB_READ_ERROR,
    SUCCESS,
    __app_name__,
    __version__,
    cli,
    qklist,
)

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

@pytest.fixture
def mock_json_file(tmp_path):
    qklistitem = [{"Description": "Sample List Item", "Priority": 2, "Done": False}]
    db_file = tmp_path / "qklist.json"
    with db_file.open("w") as db:
        json.dump(qklistitem, db, indent=4)
    return db_file

test_data1 = {
    "description": ["Clean", "the", "house"],
    "priority": 1,
    "qklistitem": {
        "Description": "Clean the house.",
        "Priority": 1,
        "Done": False,
    },
}
test_data2 = {
    "description": ["Wash the car"],
    "priority": 2,
    "qklistitem": {
        "Description": "Wash the car.",
        "Priority": 2,
        "Done": False,
    },
}

@pytest.mark.parametrize(
    "description, priority, expected",
    [
        pytest.param(
            test_data1["description"],
            test_data1["priority"],
            (test_data1["qklistitem"], SUCCESS),
        ),
        pytest.param(
            test_data2["description"],
            test_data2["priority"],
            (test_data2["qklistitem"], SUCCESS),
        ),
    ],
)
def test_add(mock_json_file, description, priority, expected):
    qklistobj = qklist.QkListObj(mock_json_file)
    assert qklistobj.add(description, priority) == expected
    read = qklistobj._db_handler.read_qklists()
    assert len(read.qk_list) == 2
