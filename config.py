from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
API_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("APP_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session = os.environ.get("TERMUX")
SESSION = os.environ.get("TERMUX")
token = os.environ.get("TOKEN")
a = TelegramClient(StringSession(session), API_ID, API_HASH)
bot = TelegramClient("bot", APP_ID, API_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
