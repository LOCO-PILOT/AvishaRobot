import requests
from telegram import ParseMode
from telegram.ext import CommandHandler

import random
from AvishaRobot import dispatcher


def waifu(update, context):
    try:
        msg = update.effective_message
        # API (DON'T EDIT)
        url = f'https://api.animeepisode.org/waifu/'
        result = requests.get(url).json()
        img = result['Character_Image']
        # Message (EDIT THIS PART AS HTML *IF YOU WANT*)
        text = f'''
<b>⬤ ɴᴀᴍᴇ ➥</b> <code>{result['Character_Name']}</code>
        
<b>⬤ ᴀɴɪᴍᴇ ➥</b> <code>{result['Anime_name']}</code>
'''
        msg.reply_photo(photo=img, caption=text, parse_mode=ParseMode.HTML)

    except Exception as e:
        text = f'<b>⬤ ᴇʀʀᴏʀ</b> ➥ <code>' + e + '</code>'
        msg.reply_text(text, parse_mode=ParseMode.HTML)


WAIFUINFO_HANDLER = CommandHandler('waifuinfo', waifu, run_async=True)
dispatcher.add_handler(WAIFUINFO_HANDLER)


__mod_name__ = "ᴡᴀɪғᴜs"

__handlers__ = [WAIFUINFO_HANDLER]
