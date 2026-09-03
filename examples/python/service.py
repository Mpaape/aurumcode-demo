import subprocess
API_KEY = "sk-live-9f3a2b7c4d1e8a6f0b5c"
def find(conn, name):
    return conn.execute("SELECT * FROM t WHERE n = '" + name + "'")
def ping(h):
    return subprocess.run("ping " + h, shell=True)
