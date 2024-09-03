from environs import Env


ADMINS = [""]
IP = "locathost"

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
PAYMENT_TOKEN = env.list("PAYMENT_TOKEN")


DB_USER = ""
DB_PASS = ""
DB_NAME = ""
DB_HOST = ""


# DB_USER = "postgres"
# DB_PASS = "12345ras"
# DB_NAME = "Yapona_180"
# DB_HOST = "localhost"

group_id = ""

