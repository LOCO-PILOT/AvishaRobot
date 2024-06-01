from pyrogram import Client, enums, filters, idle

import re
from requests import get
import asyncio
from AvishaRobot import pbot as avisha

from pyrogram.types import InlineKeyboardButton as ikb, InlineKeyboardMarkup as ikm, Message
from pyrogram.enums import ChatAction, ParseMode
import pyshorteners
shortener = pyshorteners.Shortener()
from pyrogram.handlers import MessageHandler
@avisha.on_message(filters.command(["short"]))
async def short_urls(bot, message):
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    if len(message.command) < 2:
        return await message.reply_text(
            "**⬤ ᴇxᴀᴍᴘʟᴇ ➥** `/short [url]`")
#     url_pattern = re.compile(r'https?://\S+')
    link=message.command[1]
                         
    try:

        tiny_link = shortener.tinyurl.short(link)


        dagd_link = shortener.dagd.short(link)

        clckru_link = shortener.clckru.short(link)

        shorted=[tiny_link,dagd_link,clckru_link]
        url=[
        [ikb("ᴛɪɴʏ ᴜʀʟ",url=tiny_link)],

        [ikb("ᴅᴀɢᴅ ᴜʀʟ",url=dagd_link),

         ikb("ᴄʟᴄᴋʀᴜ ᴜʀʟ",url=clckru_link)
        ]
        ]
        await message.reply_text(f"⬤ ʜᴇʀᴇ ᴀʀᴇ ғᴇᴡ sʜᴏʀᴛᴇɴᴇᴅ ʟɪɴᴋs ⏤͟͟͞͞★ ",reply_markup=ikm(url))

    except Exception as e:
        await message.reply_text(f"⬤ ᴇɪᴛʜᴇʀ ᴛʜᴇ ʟɪɴᴋ ɪs ᴀʟʀᴇᴀᴅʏ sʜᴏʀᴛᴇɴᴇᴅ ᴏʀ ɪs ɪɴᴠᴀʟɪᴅ.")

@avisha.on_message(filters.command(["unshort"]))
async def unshort(bot, message):
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    if len(message.command) < 2:
        return await message.reply_text(
            "⬤ **ᴇxᴀᴍᴘʟᴇ ➥** `/unshort [short - url]`")
    link=message.text.split(' ')[1]
    
    try:

        x = get(link, allow_redirects=True).url

        url=[

        [ikb

         ("ᴠɪᴇᴡ ʟɪɴᴋ",url=x)

        ]

        ]

        

        await message.reply_text(f"⬤ ʜᴇʀᴇ's ᴛʜᴇ ᴜɴsʜᴏʀᴛᴇɴᴇᴅ ʟɪɴᴋ ⏤͟͟͞͞★\n\n➥ `{x}` " ,reply_markup=ikm(url))

        

    except Exception as e:

        await message.reply_text(f"⬤ ᴇʀʀᴏʀ ➥ {e} ")

__help__ = """
 
 ⬤ /short <url> ➥ `/short https://t.me/roy_editx`.
 *"""

__mod_name__ = "sʜᴏʀᴛ"
