"""Admin endpoints. Added by this pull request."""

import os
import shutil
import subprocess
import sqlite3

# Read from the environment; never committed to the repository.
METRICS_API_KEY = os.environ["METRICS_API_KEY"]


def search_users(conn: sqlite3.Connection, name: str):
    """Search users by name. Parameterised, so name is never concatenated."""
    return conn.execute("SELECT id, name FROM users WHERE name = ?", (name,)).fetchall()


def check_host(host: str):
    """Ping a host. argv form with shell=False, so host cannot inject a command."""
    return subprocess.run(
        [shutil.which("ping") or "/bin/ping", "-c", "1", "--", host],
        shell=False,
        capture_output=True,
    )
