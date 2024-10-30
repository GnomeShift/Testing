import pytest
import sqlite3

@pytest.fixture(scope="function")
def sqlite_fixture():
    connection = sqlite3.connect(":memory:")
    yield connection
    connection.close()
