import json
import requests
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message
from AvishaRobot import pbot as app


@app.on_message(filters.command("bimg"))
def bingimg_search(client: Client, message: Message):
    try:
        text = message.text.split(None, 1)[
            1
        ]  
    except IndexError:
        return message.reply_text(
            "⬤ ᴘʀᴏᴠɪᴅᴇ ᴍᴇ ᴀ ǫᴜᴇʀʏ ᴛᴏ sᴇᴀʀᴄʜ!"
        )  

    search_message = message.reply_text(
        "⚡"
    )  

    url = "https://sugoi-api.vercel.app/bingimg?keyword=" + text
    resp = requests.get(url)
    images = json.loads(resp.text)

    media = []
    count = 0
    for img in images:
        if count == 6:
            break

        media.append(InputMediaPhoto(media=img))
        count += 1

    message.reply_media_group(media=media)

    search_message.delete()
    message.delete()
####

__mod_name__ = "ɪᴍᴀɢᴇ"

__help__ = """

 ⬤ /bimg ➥ sᴇᴀʀᴄʜ ᴘɪɴᴛᴇʀᴇsᴛ ɪᴍᴀɢᴇs ᴄᴏʟʟᴇᴄᴛɪᴏɴ.
 ⬤ /img ➥ sᴇᴀʀᴄʜ ɢᴏᴏɢʟᴇ ɪᴍᴀɢᴇs ᴄᴏʟʟᴇᴄᴛɪᴏɴ.
 ⬤ /rp ➥ ʀᴀɴᴅᴏᴍ ᴡᴀʟʟᴘᴀᴘᴇʀ ɪᴍᴀɢᴇ.
 ⬤ /pic <query> ➥ sᴇᴀʀᴄʜ ᴏᴡɴ ǫᴜᴇʀʏ ɪᴍᴀɢᴇ [● ᴇx ➣ /pic Tajmahal].
 """

