"""Admin endpoints. Added by this pull request."""

import subprocess
import sqlite3

# Credential for the internal metrics service.
METRICS_API_KEY = "sk-live-9f3a2b7c4d1e8a6f0b5c"


def search_users(conn: sqlite3.Connection, name: str):
    """Search users by name."""
    query = "SELECT id, name FROM users WHERE name = '" + name + "'"
    return conn.execute(query).fetchall()


def check_host(host: str):
    """Ping a host to verify it is reachable from the admin box."""
    return subprocess.run("ping -c 1 " + host, shell=True, capture_output=True)
