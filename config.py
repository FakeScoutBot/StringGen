from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 6878311635))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+rFrVYWJbaCsxNzRl")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+v1ubYvri73owZDk9")
