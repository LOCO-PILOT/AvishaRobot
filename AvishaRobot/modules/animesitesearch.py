import html

import bs4
import requests
from AvishaRobot import dispatcher
from AvishaRobot.modules.disable import DisableAbleCommandHandler
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode,
                      Update)
from telegram.ext import CallbackContext

info_btn = "ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ"
kayo_btn = "ᴋᴀʏᴏ 〠"
animespot_btn = "ᴀɴɪᴍᴇsᴘᴏᴛ 𓁔"
animetm_btn = "ᴀɴɪᴍᴇᴛᴍ 𓁔"
prequel_btn = "◁ ᴘʀᴇǫᴜᴇʟ"
sequel_btn = "sᴇǫᴜᴇʟ ▷"
close_btn = "ᴄʟᴏsᴇ ✘"


def site_search(update: Update, context: CallbackContext, site: str):
    message = update.effective_message
    args = message.text.strip().split(" ", 1)
    more_results = True

    try:
        search_query = args[1]
    except IndexError:
        message.reply_text("⬤ ɢɪᴠᴇ sᴏᴍᴛʜɪɴɢ ғᴏʀ sᴇᴀʀᴄʜ...")
        return

    if site == "kayo":
        search_url = f"https://animekayo.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"})

        result = f"❖ <b>sᴇᴀʀᴄʜ ʀᴇsᴜʟᴛ ғᴏʀ</b> <code>{html.escape(search_query)}</code> <b>ᴏɴ</b> <code>ᴀɴɪᴍᴇᴋᴀʏᴏ</code> ⏤͟͟͞͞★\n"
        for entry in search_result:

            if entry.text.strip() == "❖ ɴᴏᴛ ғᴏᴜɴᴅ...":
                result = f"❖ <b>ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ғᴏʀ</b> <code>{html.escape(search_query)}</code> <b>ᴏɴ</b> <code>ᴀɴɪᴍᴇᴋᴀʏᴏ</code> ⏤͟͟͞͞★"
                more_results = False
                break

            post_link = entry.a['href']
            post_name = html.escape(entry.text.strip())
            result += f"❖ <a href='{post_link}'>{post_name}</a>\n"
            
    elif site == "animespot":
        search_url = f"https://dubspotteam.blogspot.com/?q={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"}) 
        
        result = f"❖ <b>sᴇᴀʀᴄʜ ʀᴇsᴜʟᴛ ғᴏʀ</b> <code>{html.escape(search_query)}</code> <b>ᴏɴ</b> <code>ᴀɴɪᴍᴇsᴘᴏᴛᴅᴜʙʙᴇʀ</code> ⏤͟͟͞͞★ \n"
        for entry in search_result:
                 
           if entry.text.strip() == "❖ ɴᴏᴛ ғᴏᴜɴᴅ...":
                result = f"❖ <b>ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ғᴏʀ</b> <code>{html.escape(search_query)}</code> <b>ᴏɴ</b> <code>ᴀɴɪᴍᴇsᴘᴏᴛ</code> ⏤͟͟͞͞★"
                more_results = False
                break
                
           post_link = entry.a['href']
           post_name = html.escape(entry.text.strip())
           result += f"❖ <a href='{post_link}'>{post_name}</a>\n"
           
    elif site == "animetm":
        search_url = f"https://animetmdubbers.in/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"}) 
        
        result = f"❖ <b>sᴇᴀʀᴄʜ ʀᴇsᴜʟᴛ ғᴏʀ</b> <code>{html.escape(search_query)}</code> <b>ᴏɴ</b> <code>ᴀɴɪᴍᴇᴛᴍᴅᴜʙʙᴇʀ</code> ⏤͟͟͞͞★  \n"
        for entry in search_result:
                 
           if entry.text.strip() == "❖ ɴᴏᴛ ғᴏᴜɴᴅ...":
                result = f"❖ <b>ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ғᴏʀ</b> <code>{html.escape(search_query)}</code> <b>ᴏɴ</b> <code>ᴀɴɪᴍᴇᴋᴀʏᴏ</code>"
                more_results = False
                break
                
           post_link = entry.a['href']
           post_name = html.escape(entry.text.strip())
           result += f"❖ <a href='{post_link}'>{post_name}</a>\n"
           
    buttons = [[InlineKeyboardButton("sᴇᴇ ᴀʟʟ ʀᴇsᴜʟᴛs", url=search_url)]]

    if more_results:
        message.reply_text(
            result,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True)
    else:
        message.reply_text(
            result, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def kayo(update: Update, context: CallbackContext):
    site_search(update, context, "kayo")
    
def animespot(update: Update, context: CallbackContext):
    site_search(update, context, "animespot")
   
def animetm(update: Update, context: CallbackContext):
    site_search(update, context, "animetm")


__help__ = """

⬤ /animetm ➥ Find anime from animetm dubbers website.
⬤ /animespot ➥ Find anime from animespot website.
⬤ /kayo ➥ Find anime from animekayo website.
⬤ /latest ➥ ᴛᴏ sᴇᴇ ʟᴀᴛᴇsᴛ ᴀɴɪᴍᴇ ᴇᴘɪsᴏᴅᴇ
"""
    
__mod_name__ = "ᴀɴɪᴍᴇ-s"
KAYO_SEARCH_HANDLER = DisableAbleCommandHandler("kayo", kayo, run_async = True)
ANIMESPOT_SEARCH_HANDLER = DisableAbleCommandHandler("animespot", animespot, run_async = True)
ANIMETM_SEARCH_HANDLER = DisableAbleCommandHandler("animetm", animetm, run_async = True)

dispatcher.add_handler(KAYO_SEARCH_HANDLER)
dispatcher.add_handler(ANIMESPOT_SEARCH_HANDLER)
dispatcher.add_handler(ANIMETM_SEARCH_HANDLER)

__handlers__ = [ KAYO_SEARCH_HANDLER,
     ANIMESPOT_SEARCH_HANDLER,  ANIMETM_SEARCH_HANDLER]

                                                            
