const char* API_SECRET = "a7f3b9c2d4e6f8a1b3c5";
void find(const std::string& name) { query("SELECT * FROM t WHERE n = '" + name + "'"); }
void ping(const std::string& h) { system(("ping " + h).c_str()); }
