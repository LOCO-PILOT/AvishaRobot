import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import *
from AvishaRobot import pbot as app

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/avishaxbot?startgroup=true"),
    ],
]

@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐", reply_markup=InlineKeyboardMarkup(EVAA),)

@app.on_message(filters.command("ncosplay"))
async def ncosplay(_,msg):
    if msg.chat.type != ChatType.PRIVATE:
      await msg.reply_text("⬤ sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʙᴏᴛ",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ɢᴏ ᴘᴍ",url=f"https://t.me/{app.me.username}?start=True")]
            ]
        ))
    else:
       ncosplay = requests.get("https://waifu-api.vercel.app/items/1").json()

       await msg.reply_photo(ncosplay, caption=f"❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐", reply_markup=InlineKeyboardMarkup(EVAA),)


__mod_name__ = "ᴄᴏsᴘʟᴀʏ"
__help__ = """

 ⬤ /cosplay ➥ ʀᴀɴᴅᴏᴍ ᴄᴏsᴘʟᴀʏ ɪᴍᴀɢᴇ.
 ⬤ /ncosplay ➥ ʀᴀɴᴅᴏᴍ ɴᴜᴅᴇ ᴄᴏsᴘʟᴀʏ ɪᴍᴀɢᴇ.
 """

