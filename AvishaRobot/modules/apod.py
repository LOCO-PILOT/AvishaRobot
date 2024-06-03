from AvishaRobot import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler
import requests

APOD_API_KEY = "owYBQUGZBWCyHpC8bacQcseCLifb2j2B2wPxxKo9"

def apod(update: Update, context: CallbackContext):
    # Attempt to fetch data from the NASA APOD API
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={APOD_API_KEY}')
    
    if response.status_code == 200:
        result = response.json()
        img = result.get('hdurl')  # Using get to avoid KeyError if 'hdurl' is missing
        title = result.get('title', 'ɴᴏ ᴛɪᴛʟᴇ ᴀᴠᴀɪʟᴀʙʟᴇ')  # Default title
        
        # Handling missing copyright information gracefully
        copyright = result.get('copyright', 'ᴄᴏᴘʏʀɪɢʜᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ')
        
        url = 'https://apod.nasa.gov/apod/'
        text = f'❖ <b>ᴛɪᴛʟᴇ ➥ {title}</b>\n\n● <i>ᴄʀᴇᴅɪᴛs ➥ {copyright}</i>\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐'
        
        # Ensure there's an image URL before trying to send it
        if img:
            update.effective_message.reply_photo(
                img, 
                caption=text, 
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴍᴏʀᴇ ɪɴғᴏ", url=url)]]),
                parse_mode=ParseMode.HTML
            )
        else:
            update.effective_message.reply_text("❖ ɴᴏ ɪᴍᴀɢᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛᴏᴅᴀʏ.")
    else:
        update.effective_message.reply_text("⬤ ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴛʜᴇ ᴀᴘᴏᴅ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.")

apod_handler = CommandHandler("apod", apod, run_async=True)
dispatcher.add_handler(apod_handler)

__mod_name__ = "ɴᴀsᴀ"

__help__ = """

⬤ /apod ➥ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴀsᴛʀᴏɴᴏᴍʏ ᴘɪᴄᴛᴜʀᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ ʙʏ ɴᴀsᴀ.
"""
