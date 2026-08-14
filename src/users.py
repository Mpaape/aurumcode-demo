"""User lookup helpers."""

import sqlite3


def connect(path: str) -> sqlite3.Connection:
    return sqlite3.connect(path)


def get_user(conn: sqlite3.Connection, uid: int):
    """Look a user up by id. Parameterised, so uid is never concatenated."""
    return conn.execute("SELECT id, name FROM users WHERE id = ?", (uid,)).fetchone()


def list_users(conn: sqlite3.Connection):
    return conn.execute("SELECT id, name FROM users ORDER BY id").fetchall()
