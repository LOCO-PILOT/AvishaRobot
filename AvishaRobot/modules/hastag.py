import requests
from bs4 import BeautifulSoup as  BSP
from AvishaRobot import pbot as app
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram import filters


EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/Avishaxbot?startgroup=true"),
    ],
]

######

url = "https://all-hashtag.com/library/contents/ajax_generator.php"

@app.on_message(filters.command("hastag"))
async def hastag(bot, message):
    global content
    try:
        text = message.text.split(' ',1)[1]
        data = dict(keyword=text, filter="top")

        res = requests.post(url, data).text

        content = BSP(res, 'html.parser').find("div", {"class":"copy-hashtags"}).string
    except IndexError:
        return await message.reply_text("⬤ Example ➥ /hastag instagram")
        
    
    await message.reply_text(f"❖ ʜᴇʀᴇ ɪs ʏᴏᴜʀ  ʜᴀsᴛᴀɢ ➥\n\n<pre>{content}</pre>",reply_markup=InlineKeyboardMarkup(EVAA), quote=True)
    
#####

__help__ = """

⬤ /figlet ➥ ᴍᴀᴋᴇs ғɪɢʟᴇᴛ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
⬤ /qr ➥ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ǫʀᴄᴏᴅᴇ.
⬤ /hastag ➥ ɢᴇɴʀᴀᴛᴇ ʀᴀɴᴅᴏᴍ #ʜᴀsʜᴛᴀɢ.
"""

__mod_name__ = "ғɪɢʟᴇᴛ"
