
from telethon import Button
from AvishaRobot import telethn
from AvishaRobot.events import register

PHOTO = "https://graph.org/file/4126cda3b1ff1c43f70aa.mp4"


@register(pattern=("Good evening"))
async def awake(event):
    NEKO = f"❖ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ᴇᴠᴇɴɪɴɢ ❖\n\n● ᴇᴠᴇɴɪɴɢs ᴀʀᴇ ᴛʜᴇ ʙᴇᴀᴜᴛɪғᴜʟʟʏ sᴡᴇᴇᴛ sᴘᴏᴛ ʙᴇᴛᴡᴇᴇɴ ᴛʜᴇ ʜᴀʀsʜ ʟɪɢʜᴛ ᴏғ ᴛʜᴇ ᴅᴀʏ ᴀɴᴅ ᴛʜᴇ ᴅᴇᴀᴅ ᴅᴀʀᴋɴᴇss ᴏғ ɴɪɢʜᴛ.\n\n● ᴡɪsʜɪɴɢ ᴛᴏ ➥ {event.sender.first_name}\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ [๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐](https://t.me/avishaxbot)"
    BUTTON = [
        [
            Button.url("ᴍᴇᴇᴛ ᴍᴇ ʜᴇʀᴇ ʙᴀʙʏ", "https://telegram.dog/The_Friendz"),
        ]
    ]
    await telethn.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
  
