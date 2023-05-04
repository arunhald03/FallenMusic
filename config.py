from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("25764824"))
API_HASH = getenv("637550d4edbe66606d184abbe961d0f5")

BOT_TOKEN = getenv("BOT_TOKEN", "2144094143:AAEbn55ufmFNwbuoXpdUQ5m_24ugEnXztd0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID","868753606"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Tamilchat_tgk")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Smart_aruney_143")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "868753606").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
