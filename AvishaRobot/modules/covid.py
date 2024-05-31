import datetime
import requests
import os
import re
import urllib
import urllib.request

from datetime import datetime
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from random import randint
from typing import List
from telegram import ParseMode, InputMediaPhoto, Update, TelegramError, ChatAction
from telegram.ext import CommandHandler, run_async, CallbackContext

from AvishaRobot import dispatcher
from AvishaRobot.modules.disable import DisableAbleCommandHandler


def covid(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text.split(' ', 1)
    try:
       if len(text) == 1:
           r = requests.get("https://disease.sh/v3/covid-19/all").json()
           reply_text = f"**✜ ɢʟᴏʙᴀʟ ᴛᴏᴛᴀʟs** 🦠 ✜\n\n● ᴄᴀsᴇs ➥ {r['cases']:,}\n● ᴛᴏᴅᴀʏ ᴄᴀsᴇs ➥ {r['todayCases']:,}\n● ᴅᴇᴀᴛʜs ➥ {r['deaths']:,}\n● ᴛᴏᴅᴀʏ ᴅᴇᴀᴛʜs ➥ {r['todayDeaths']:,}\n● ʀᴇᴄᴏᴠᴇʀᴇᴅ ➥ {r['recovered']:,}\n● ᴀᴄᴛɪᴠᴇ ➥ {r['active']:,}\n● ᴄʀɪᴛɪᴄᴀʟ ➥ {r['critical']:,}\n● ᴄᴀsᴇs/ᴍɪʟ ➥ {r['casesPerOneMillion']}\n● ᴅᴇᴀᴛʜs/ᴍɪʟ ➥ {r['deathsPerOneMillion']}"
       else:
           variabla = text[1]
           r = requests.get(
               f"https://disease.sh/v3/covid-19/countries/{variabla}").json()
           reply_text = f"**❖ ᴄᴏʀᴏɴᴀ ᴄᴀsᴇs ғᴏʀ {r['country']} 🦠** ❖\n\n● ᴄᴀsᴇs ➥ {r['cases']:,}\n● ᴛᴏᴅᴀʏ ᴄᴀsᴇs ➥ {r['todayCases']:,}\n● ᴅᴇᴀᴛʜs ➥ {r['deaths']:,}\n● ᴛᴏᴅᴀʏ ᴅᴇᴀᴛʜs ➥ {r['todayDeaths']:,}\n● ʀᴇᴄᴏᴠᴇʀᴇᴅ ➥ {r['recovered']:,}\n● ᴀᴄᴛɪᴠᴇ ➥ {r['active']:,}\n● ᴄɪʀᴛɪᴄᴀʟ ➥ {r['critical']:,}\n● ᴄᴀsᴇs/ᴍɪʟ ➥ {r['casesPerOneMillion']}\n● ᴅᴇᴀᴛʜs/ᴍɪʟ ➥ {r['deathsPerOneMillion']}\n\n✦ ᴄᴏᴠɪᴅ ʀᴇᴘᴏʀᴛ ʙʏ ➥ ᴀ ᴠ ɪ s ʜ ᴀ ࿐ "
       message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)
    except Exception:
        return msg.reply_text("❖ ᴛʜᴇʀᴇ ᴡᴀs ᴀ ᴘʀᴏʙʟᴀᴍ ᴡʜɪʟᴇ ɪᴍᴘᴏʀᴛɪɴɢ ᴛʜᴇ ᴅᴀᴛᴀ.")


COVID_HANDLER = DisableAbleCommandHandler(["covid", "corona"], covid, run_async = True)
dispatcher.add_handler(COVID_HANDLER)

#####

__mod_name__="ᴄᴏᴠɪᴅ¹⁹"

__help__="""

 ❍ /covid ➛ ᴄʜᴇᴀᴄᴋ ᴄᴏᴠɪᴅ ᴄᴀsᴇs ɪɴ ʏᴏᴜʀ ᴄᴏᴜɴᴛʀʏ.
 """
