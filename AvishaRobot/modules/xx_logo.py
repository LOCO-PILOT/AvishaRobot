from pyrogram.types import Message
import random
from pyrogram import Client, filters, idle
import pyrogram, asyncio, random, time
from pyrogram.errors import FloodWait
import requests
from AvishaRobot import pbot as app
from pyrogram.types import *

button = [
       [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/AvishaXbot?startgroup=true",
            )
        ]
]
#####



######
@app.on_message(filters.command("mlogo"))
async def logo(app, msg: Message):
    if len(msg.command) == 1:
       return await msg.reply_text("✦ ᴜsᴀɢᴇ ➥ /mlogo Avisha")
    logo_name = msg.text.split(" ", 1)[1]
    API = f"https://api.sdbots.tech/logohq?text={logo_name}"
    req = requests.get(API).url
    await msg.reply_photo(
        photo=f"{req}",
        caption=f"❖ ʟᴏɢᴏ ʙʏ ➥ [๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐](https://t.me/the_friendz)",
        reply_markup=InlineKeyboardMarkup(button),
    )


#######

