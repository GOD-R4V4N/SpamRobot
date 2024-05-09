import logging

from telethon import TelegramClient

from os import getenv
from Asuraa.data import MAHAK


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 20851717
API_HASH = "0217fe5cd94ff3f4d4555b1551670144"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)


SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6927241780").split()))
for x in MAHAK:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6927241780"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
