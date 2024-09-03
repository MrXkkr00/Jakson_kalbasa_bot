from environs import Env


ADMINS = ["7010118152"]
IP = "locathost"

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
PAYMENT_TOKEN = env.list("PAYMENT_TOKEN")


DB_USER = "botlaru1_jakson_user"
DB_PASS = "jakson_user"
DB_NAME = "botlaru1_jakson_db"
DB_HOST = "localhost"


# DB_USER = "postgres"
# DB_PASS = "12345ras"
# DB_NAME = "Yapona_180"
# DB_HOST = "localhost"

group_id = "-1002204397362"

