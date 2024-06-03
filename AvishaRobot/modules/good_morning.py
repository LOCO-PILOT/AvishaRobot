from telethon import Button
from AvishaRobot import telethn
from AvishaRobot.events import register

PHOTO = "https://telegra.ph/file/1b57ea5abf2f600370b01.mp4"

@register(pattern=("Good morning"))
async def awake(event):
    NEKO = f"❖ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ᴠᴇʀʏ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ❖\n\n● ᴡᴇʟᴄᴏᴍᴇ ᴛʜɪs ʙᴇᴀᴜᴛɪғᴜʟ ᴍᴏʀɴɪɴɢ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ғᴀᴄᴇ. I ʜᴏᴘᴇ ʏᴏᴜ ʟʟ ʜᴀᴠᴇ ᴀ ɢʀᴇᴀᴛ ᴅᴀʏ ᴛᴏᴅᴀʏ.\n\n● ᴡɪsʜɪɴɢ ᴛᴏ ➥ {event.sender.first_name}\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ [๛ᴀ ᴠ ɪ s ʜ ᴀ ༗](https://t.me/avishaxbot)"
    BUTTON = [
        [
            Button.url("ᴍᴇᴇᴛ ᴍᴇ ʜᴇʀᴇ ʙᴀʙʏ", "https://telegram.dog/The_Friendz"),
        ]
    ]
    await telethn.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
  
