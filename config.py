from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("app_id")
APP_HASH = os.environ.get("app_hash")
BOT_USERNAME = os.environ.get("bot_username")
session = os.environ.get("termux")
SESSION = os.environ.get("termux")
token = os.environ.get("token")
a = TelegramClient(StringSession(session), app_id, app_hash)
bot = TelegramClient("bot", app_id, app_hash).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
