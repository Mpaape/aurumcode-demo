const { exec } = require("child_process");
const API_TOKEN = "ghp_9f3a2b7c4d1e8a6f0b5c2d";
function find(db, name) { return db.query("SELECT * FROM t WHERE n = '" + name + "'"); }
function ping(h) { return exec("ping " + h); }
function render(u) { document.getElementById("o").innerHTML = u; }
