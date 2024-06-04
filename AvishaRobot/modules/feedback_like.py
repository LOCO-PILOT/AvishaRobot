import random

from telegram import ParseMode
from telethon import Button

from AvishaRobot import OWNER_ID, SUPPORT_CHAT
from AvishaRobot import telethn as tbot

from ..events import register


@register(pattern="/feedback ?(.*)")
async def feedback(e):
    quew = e.pattern_match.group(1)
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    HOTTIE = (
        "https://graph.org/file/f86b71018196c5cfe7344.jpg",
        "https://graph.org/file/a3db9af88f25bb1b99325.jpg",
        "https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
        "https://graph.org/file/84de4b440300297a8ecb3.jpg",
        "https://graph.org/file/84e84ff778b045879d24f.jpg",
        "https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
        "https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
        "https://graph.org/file/d6360613d0fa7a9d2f90b.jpg",
        "https://graph.org/file/9bba2b7ee9ba3806de65d.jpg",
        "https://graph.org/file/ef82f289043a4fa74f8ff.jpg",
        "https://graph.org/file/9c27c68958e06ae074c38.jpg",
        "https://graph.org/file/0ff325b1d2efe80299aa3.jpg",
        "https://graph.org/file/41167b953cf3579853d47.jpg",
        "https://graph.org/file/bd93ab42e69305f274028.jpg",
        "https://graph.org/file/97575db5586c05d6b2898.jpg",
        "https://graph.org/file/07c393fdf931a407c9bc0.jpg",
        "https://graph.org/file/f332767490ad3a5ca20e8.jpg",
        "https://graph.org/file/f3449e9069667f647d14e.jpg",
        "https://graph.org/file/9f51cdc739f907cbd2c7e.jpg",
        "https://telegra.ph/file/d7a6a923c38e051ce35f3.jpg",
    )
    FEED = ("https://graph.org/file/d6360613d0fa7a9d2f90b.jpg", )
    BUTTON = [[
        Button.url("ɢᴏ ᴛᴏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", f"https://t.me/{SUPPORT_CHAT}")
    ]]

    TEXT = "❖ ᴛʜᴀɴᴋs ғᴏʀ ʏᴏᴜʀ ғᴇᴇᴅʙᴀᴄᴋ, ɪ ʜᴏᴘᴇ ʏᴏᴜ ʜᴀᴘᴘʏ ᴡɪᴛʜ ᴏᴜʀ sᴇʀᴠɪᴄᴇ."
    GIVE = "⬤ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ғᴏʀ ғᴇᴇᴅʙᴀᴄᴋ."
    logger_text = f"""
**❖ ɴᴇᴡ ғᴇᴇᴅʙᴀᴄᴋ ❖**

**● ғʀᴏᴍ ᴜsᴇʀ ➥** {mention}
**● ᴜsᴇʀɴᴀᴍᴇ ➥** @{e.sender.username}
**● ᴜsᴇʀ ɪᴅ ➥** `{e.sender.id}`
**● ғᴇᴇᴅʙᴀᴄᴋ ➥** `{e.text}`

**❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ** ➥ [๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐](https://t.me/avishaxbot)
"""
    if user_id == 6142770593:
        await e.reply("**⬤ sʀʏ ɪ ᴄᴀɴ'ᴛ ɪᴅᴇɴᴛɪғʏ ʏᴏᴜʀ ɪɴғᴏ.**",
                      parse_mode=ParseMode.MARKDOWN)
        return

    if user_id == 1087968824:
        await e.reply("**⬤ ᴛᴜʀɴ ᴏғғ ᴜʀ ᴀɴᴏɴʏᴍᴏᴜs ᴍᴏᴅᴇ ᴀɴᴅ ᴛʀʏ.**",
                      parse_mode=ParseMode.MARKDOWN)
        return

    if e.sender_id != OWNER_ID and not quew:
        await e.reply(
            GIVE,
            parse_mode=ParseMode.MARKDOWN,
            buttons=BUTTON,
            file=random.choice(HOTTIE),
        ),
        return

    await tbot.send_message(
        SUPPORT_CHAT,
        f"{logger_text}",
        file=random.choice(HOTTIE),
        link_preview=False,
    )
    await e.reply(TEXT, file=random.choice(HOTTIE), buttons=BUTTON)


__mod_name__ = "ғᴇᴇᴅʙᴀᴄᴋ"

__help__ = """

 ⬤ /feedback ➥ ɢɪᴠᴇ ғᴇᴇᴅʙᴀᴄᴋ ᴛᴏ ᴀᴠɪsʜᴀ ʙᴏᴛ.
 """
