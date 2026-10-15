public class Repo {
    private const string DB_PASSWORD = "Pa55w0rd9xKq2mZt";
    public void Find(string name) { cmd.CommandText = "SELECT * FROM users WHERE n = '" + name + "'"; }
    public void Ping(string h) { Process.Start("sh", "-c \"ping " + h + "\""); }
}
