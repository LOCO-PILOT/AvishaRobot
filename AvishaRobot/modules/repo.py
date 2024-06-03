from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from AvishaRobot import OWNER_ID, dispatcher
from AvishaRobot import pbot as client
from AvishaRobot import pbot as app 

AVISHA = "https://graph.org/file/dcc62e53435a919373a0a.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=AVISHA,
        caption=f"""❖ ʜᴇʏ {message.from_user.mention()}, ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ ♥︎\n\n⬤ ɪғ ʏᴏᴜ ᴡᴀɴᴛ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username}) ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username}) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ",user_id=OWNER_ID
                    ),
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ",
                        callback_data="gib_source",
                    ),
                ]
            ]
        ),
    )


@app.on_callback_query(filters.regex("gib_source"))
async def gib_repo_callback(_, callback_query):
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://telegra.ph/file/9235d57807362b4e227a3.mp4", has_spoiler=True),
        reply_markup=InlineKeyboardMarkup(
            [
                [close_button]
            ]
        ),
        )
close_button = InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")

@app.on_callback_query(filters.regex("close"))
async def close_menu(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except:
        return

