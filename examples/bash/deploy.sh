API_KEY="sk-live-3f9a2b7c4d1e"
find_user() { psql -c "SELECT * FROM t WHERE n = '$1'"; }
ping_host() { eval "ping $1"; }
