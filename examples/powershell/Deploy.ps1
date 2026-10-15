$ApiToken = "ghp9f3a2b7c4d1e8a6f0b"
function Find-User { param($n) Invoke-Sqlcmd -Query ("SELECT * FROM t WHERE n = '" + $n + "'") }
function Ping-Host { param($h) Invoke-Expression ("ping " + $h) }
