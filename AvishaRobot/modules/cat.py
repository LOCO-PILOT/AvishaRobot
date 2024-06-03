import requests
from pyrogram import filters
from pyrogram.types import CallbackQuery, InputMediaPhoto
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.types import Message
from AvishaRobot import pbot as app

close_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ʀᴇғʀᴇsʜ", callback_data="refresh_cat"),
            InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close")
        ],
    ]
)


@app.on_message(filters.command("cat"))
async def cat(c, m: Message):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.status_code == 200:
        data = r.json()
        cat_url = data[0]["url"]
        if cat_url.endswith(".gif"):
            await m.reply_animation(
                cat_url, caption="⬤ ᴛʜɪs ɪs ᴄᴀᴛ ᴘɪᴄᴛᴜʀᴇ. ♥︎", reply_markup=close_keyboard
            )
        else:
            await m.reply_photo(cat_url, caption="⬤ ᴛʜɪs ɪs ᴄᴀᴛ ᴘɪᴄᴛᴜʀᴇ. ♥︎", reply_markup=close_keyboard)
    else:
        await m.reply_text("⬤ ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴄᴀᴛ ᴘɪᴄᴛᴜʀᴇ. 🙀")


@app.on_callback_query(filters.regex("refresh_cat"))
async def refresh_cat(c, m: CallbackQuery):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.status_code == 200:
        data = r.json()
        cat_url = data[0]["url"]
        if cat_url.endswith(".gif"):
            await m.edit_message_animation(
                cat_url, caption="⬤ ᴛʜɪs ɪs ᴄᴀᴛ ᴘɪᴄᴛᴜʀᴇ. ♥︎", reply_markup=close_keyboard
            )
        else:
            await m.edit_message_media(
                InputMediaPhoto(media=cat_url, caption="⬤ ᴛʜɪs ɪs ᴄᴀᴛ ᴘɪᴄᴛᴜʀᴇ. ♥︎"),
                reply_markup=close_keyboard,
            )
    else:
        await m.edit_message_text("⬤ ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴄᴀᴛ ᴘɪᴄᴛᴜʀᴇ. 🙀")
      
