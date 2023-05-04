from telethon.tl.functions.channels import JoinChannelRequest
from telethon import events
import asyncio
from config import *
from aLnMrod import *

a.start()
	
@a.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    await a(JoinChannelRequest("ALIBAASHAR"))
    await a(JoinChannelRequest("ABNBASHAAR"))
    await a(JoinChannelRequest("turbobh"))
    await a.send_message(event.chat_id, "لايوجد مثل هذا الأمر .!")
    await a.send_message(event.chat_id, "اوامر السورس هي \n تيربو \nturbo انواع السورس \n استخدام الاوامر يكون بدون نقطه")
    
@a.on(events.NewMessage(outgoing=True, pattern=r"stop"))
async def update(event):
    await a.send_message(event.chat_id, "The catch is cleared from the ⤷ number 1")
    await a.disconnect()

a.run_until_disconnected()
