from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","27015406"))
API_HASH = getenv("API_HASH", "4346a15e8eed59a4906886b8f40d2d71")

BOT_TOKEN = getenv("BOT_TOKEN","6008407573:AAFLkIf7prQBrqTE7np3LW-Lwo-zTUsBcNs")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://lucifer:ASShaw96@lucifer.vuows.mongodb.net/lucifer?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 1748768168))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ah07v")
