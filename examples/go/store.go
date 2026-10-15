package main
import ("database/sql"; "os/exec")
const AWS_SECRET_ACCESS_KEY = "wJalr8UtnFEMI7K9MDENGbPxRfiCY2EX"
func find(db *sql.DB, name string) { db.Query("SELECT * FROM users WHERE n = '" + name + "'") }
func ping(h string) { exec.Command("sh", "-c", "ping "+h).Run() }
