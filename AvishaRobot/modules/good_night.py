from telethon import Button

from AvishaRobot import telethn
from AvishaRobot.events import register

PHOTO = "https://graph.org/file/58b51eea6da66728915f1.mp4"


@register(pattern=("Good night"))
async def awake(event):
    NEKO = f"❖ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖\n\n● ᴍᴀʏ ᴛʜᴇ ᴀɴɢᴇʟs ғʀᴏᴍ ʜᴇᴀᴠᴇɴ ʙʀɪɴɢ ᴛʜᴇ sᴡᴇᴇᴛᴇsᴛ ᴏғ ᴀʟʟ ᴅʀᴇᴀᴍs ғᴏʀ ʏᴏᴜ. ᴍᴀʏ ʏᴏᴜ ʜᴀᴠᴇ ʟᴏɴɢ ᴀɴᴅ ʙʟɪssғᴜʟ sʟᴇᴇᴘ ғᴜʟʟ ᴏғ ʜᴀᴘᴘʏ ᴅʀᴇᴀᴍs.\n\n● ᴡɪsʜɪɴɢ ᴛᴏ ➥ {event.sender.first_name}\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ [๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐](https://t.me/avishaxbot)"
    BUTTON = [
        [
            Button.url("ᴍᴇᴇᴛ ᴍᴇ ʜᴇʀᴇ ʙᴀʙʏ", "https://telegram.dog/the_friendz"),
        ]
    ]
    await telethn.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
  
