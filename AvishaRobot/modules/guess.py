import random
from PIL import Image
from AvishaRobot import telethn as neko
from telethon import events


@neko.on(events.NewMessage(pattern="/guess ?(.*)"))
async def wish(e):

 if e.is_reply:
         mm = random.randint(1,100)
         lol = await e.get_reply_message()
         fire = "https://telegra.ph/file/060b79fec4a50f48d59ba.jpg"
         await neko.send_file(e.chat_id, fire,caption=f"**⬤ ʜᴇʏ ʙᴀʙʏ [{e.sender.first_name}](tg://user?id={e.sender.id}), ʏᴏᴜʀ ɢᴜᴇss ɪs {mm}%**\n\n⬤ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ [๛ᴀ ᴠ ɪ s ʜ ᴀ ♡゙](https://t.me/the_friendz)", reply_to=lol)
 if not e.is_reply:
         mm = random.randint(1,100)
         fire = "https://telegra.ph/file/060b79fec4a50f48d59ba.jpg"
         await neko.send_file(e.chat_id, fire,caption=f"**⬤ ʜᴇʏ ʙᴀʙʏ [{e.sender.first_name}](tg://user?id={e.sender.id}), ʏᴏᴜʀ ɢᴜᴇss ɪs {mm}%**\n\n⬤ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ [๛ᴀ ᴠ ɪ s ʜ ᴀ ♡゙](https://t.me/the_friendz)", reply_to=e)
