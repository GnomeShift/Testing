from KT3.sqlite_fixture import sqlite_fixture

def test_sqlite_fixture(sqlite_fixture):
    cursor = sqlite_fixture.cursor()
    
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    sqlite_fixture.commit()
    
    cursor.execute("INSERT INTO users (name) VALUES ('sqlite_test')")
    sqlite_fixture.commit()
    
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    assert len(result) == 1
