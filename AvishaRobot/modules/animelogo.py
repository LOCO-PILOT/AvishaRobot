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
@app.on_message(filters.command("animelogo"))
async def logo(app, msg: Message):
    if len(msg.command) == 1:
       return await msg.reply_text("⬤ ᴜsᴀɢᴇ ➥ /animelogo Avisha")
    logo_name = msg.text.split(" ", 1)[1]
    API = f"https://api.sdbots.tech/anime-logo?name={logo_name}"
    req = requests.get(API).url
    await msg.reply_photo(
        photo=f"{req}",
        caption=f"❖ ᴀɴɪᴍᴇ ʟᴏɢᴏ ʙʏ ➥ [๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐](https://t.me/the_friendz)",
        reply_markup=InlineKeyboardMarkup(button),
    )


#######

__mod_name__ = "ᴀ-ʟᴏɢᴏ"

__help__ = """

 ⬤ /animelogo ➥ ᴄʀᴇᴀᴛᴇ ᴏᴡɴ ᴛᴇxᴛ ᴀɴɪᴍᴇ ʟᴏɢᴏ.
 ⬤ /xlogo ➥ ᴄʀᴇᴀᴛᴇ ᴏᴡɴ ᴛᴇxᴛ ʟᴏɢᴏ.
 ⬤ /logo (Text) ➥ ᴄʀᴇᴀᴛᴇ ᴀ ʟᴏɢᴏ ᴏғ ʏᴏᴜʀ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴡɪᴛʜ ʀᴀɴᴅᴏᴍ ᴠɪᴇᴡ. 
 ⬤ /blackpink ➥ ᴄʀᴇᴀᴛᴇ ᴛᴇxᴛ ʟᴏɢᴏ ɪɴ ʙʟᴀᴄᴋᴘɪɴᴋ ғᴏʀᴍᴀᴛᴇ.
 ⬤ /carbon ➥ ᴄʀᴇᴀᴛᴇ ᴛᴇxᴛ ᴛᴏ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇs.
 """
