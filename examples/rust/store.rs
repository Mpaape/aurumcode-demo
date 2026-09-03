const ACCESS_KEY: &str = "AKIA9F3A2B7C4D1E8A6F";
fn find(name: &str) { conn.query(&("SELECT * FROM t WHERE n = '".to_owned() + name)); }
fn ping(h: &str) { Command::new("sh").arg("-c").arg("ping ".to_owned() + h).spawn(); }
