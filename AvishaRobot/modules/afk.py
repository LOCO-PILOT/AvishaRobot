import time, re
from AvishaRobot import BOT_USERNAME
from pyrogram.enums import MessageEntityType
from pyrogram import filters
from pyrogram.types import Message
from AvishaRobot import pbot as app
from AvishaRobot.Love.readable_time import get_readable_time
from AvishaRobot.Love.afkdb import add_afk, is_afk, remove_afk
import random 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/Avishaxbot?startgroup=true"),
    ],
]

POLICE = [
"https://graph.org/file/eaa3a2602e43844a488a5.jpg",
"https://graph.org/file/b129e98b6e5c4db81c15f.jpg",
"https://graph.org/file/3ccb86d7d62e8ee0a2e8b.jpg",
"https://graph.org/file/df11d8257613418142063.jpg",
"https://graph.org/file/9e23720fedc47259b6195.jpg",
"https://graph.org/file/826485f2d7db6f09db8ed.jpg",
"https://graph.org/file/ff3ad786da825b5205691.jpg",
"https://graph.org/file/52713c9fe9253ae668f13.jpg",
"https://graph.org/file/8f8516c86677a8c91bfb1.jpg",
"https://graph.org/file/6603c3740378d3f7187da.jpg",
"https://graph.org/file/66cb6ec40eea5c4670118.jpg",
"https://graph.org/file/2e3cf4327b169b981055e.jpg",
]

@app.on_message(filters.command(["afk"], prefixes=["/", "!", ""]))
async def active_afk(_, message: Message):
    if message.sender_chat:
        return
    user_id = message.from_user.id
    verifier, reasondb = await is_afk(user_id)
    if verifier:
        await remove_afk(user_id)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeafk)))
            if afktype == "text":
                send = await message.reply_text(
                    f"**❖ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}",
                    disable_web_page_preview=True,
                )
            if afktype == "text_reason":
                send = await message.reply_text(
                    f"**❖ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`",
                    disable_web_page_preview=True,
                )
            if afktype == "animation":
                if str(reasonafk) == "None":
                    send = await message.reply_animation(
                        data,
                        caption=f"**❖ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}",
                    )
                else:
                    send = await message.reply_animation(
                        data,
                        caption=f"**❖ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`",
                    )
            if afktype == "photo":
                if str(reasonafk) == "None":
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"**❖ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}",
                    )
                else:
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"**❖ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`",
                    )
        except Exception:
            send = await message.reply_text(
                f"**❖ {message.from_user.first_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ",
                disable_web_page_preview=True,
            )

    if len(message.command) == 1 and not message.reply_to_message:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and not message.reply_to_message:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "text_reason",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        _reason = message.text.split(None, 1)[1].strip()
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.sticker:
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
    elif len(message.command) > 1 and message.reply_to_message.sticker:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text_reason",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
    else:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }

    await add_afk(user_id, details)    
    await message.reply_photo(
        photo=random.choice(POLICE),
        caption=f"❖ {message.from_user.first_name} ɪs ɴᴏᴡ ᴀғᴋ !" , reply_markup=InlineKeyboardMarkup(EVAA),
    )




chat_watcher_group = 1


@app.on_message(
    ~filters.me & ~filters.bot & ~filters.via_bot,
    group=chat_watcher_group,
)
async def chat_watcher_func(_, message):
    if message.sender_chat:
        return
    userid = message.from_user.id
    user_name = message.from_user.first_name
    if message.entities:
        possible = ["/afk", f"/afk@{BOT_USERNAME}"]
        message_text = message.text or message.caption
        for entity in message.entities:
            if entity.type == MessageEntityType.BOT_COMMAND:
                if (message_text[0 : 0 + entity.length]).lower() in possible:
                    return

    msg = ""
    replied_user_id = 0


    
    verifier, reasondb = await is_afk(userid)
    if verifier:
        await remove_afk(userid)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeafk)))
            if afktype == "text":
                msg += f"**❖ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n"
            if afktype == "text_reason":
                msg += f"**❖ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n"
            if afktype == "animation":
                if str(reasonafk) == "None":
                    send = await message.reply_animation(
                        data,
                        caption=f"**❖ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                    )
                else:
                    send = await message.reply_animation(
                        data,
                        caption=f"**❖ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                    )
            if afktype == "photo":
                if str(reasonafk) == "None":
                    send = await message.reply_photo(
                        photo=f"downloads/{userid}.jpg",
                        caption=f"**❖ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                    )
                else:
                    send = await message.reply_photo(
                        photo=f"downloads/{userid}.jpg",
                        caption=f"**❖ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                    )
        except:
            msg += f"**❖ {user_name[:25]}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ\n\n"


    if message.reply_to_message:
        try:
            replied_first_name = message.reply_to_message.from_user.first_name
            replied_user_id = message.reply_to_message.from_user.id
            verifier, reasondb = await is_afk(replied_user_id)
            if verifier:
                try:
                    afktype = reasondb["type"]
                    timeafk = reasondb["time"]
                    data = reasondb["data"]
                    reasonafk = reasondb["reason"]
                    seenago = get_readable_time((int(time.time() - timeafk)))
                    if afktype == "text":
                        msg += (
                            f"**❖ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n"
                        )
                    if afktype == "text_reason":
                        msg += f"**❖ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n"
                    if afktype == "animation":
                        if str(reasonafk) == "None":
                            send = await message.reply_animation(
                                data,
                                caption=f"**❖ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                            )
                        else:
                            send = await message.reply_animation(
                                data,
                                caption=f"**❖ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                            )
                    if afktype == "photo":
                        if str(reasonafk) == "None":
                            send = await message.reply_photo(
                                photo=f"downloads/{replied_user_id}.jpg",
                                caption=f"**❖ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                            )
                        else:
                            send = await message.reply_photo(
                                photo=f"downloads/{replied_user_id}.jpg",
                                caption=f"**❖ {replied_first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                            )
                except Exception:
                    msg += f"**❖ {replied_first_name}** ɪs ᴀғk"
        except:
            pass

    if message.entities:
        entity = message.entities
        j = 0
        for x in range(len(entity)):
            if (entity[j].type) == MessageEntityType.MENTION:
                found = re.findall("@([_0-9a-zA-Z]+)", message.text)
                try:
                    get_user = found[j]
                    user = await app.get_users(get_user)
                    if user.id == replied_user_id:
                        j += 1
                        continue
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_afk(user.id)
                if verifier:
                    try:
                        afktype = reasondb["type"]
                        timeafk = reasondb["time"]
                        data = reasondb["data"]
                        reasonafk = reasondb["reason"]
                        seenago = get_readable_time((int(time.time() - timeafk)))
                        if afktype == "text":
                            msg += (
                                f"**❖ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n"
                            )
                        if afktype == "text_reason":
                            msg += f"**❖ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n"
                        if afktype == "animation":
                            if str(reasonafk) == "None":
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**❖ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                                )
                            else:
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**❖ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                                )
                        if afktype == "photo":
                            if str(reasonafk) == "None":
                                send = await message.reply_photo(
                                    photo=f"downloads/{user.id}.jpg",
                                    caption=f"**❖ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                                )
                            else:
                                send = await message.reply_photo(
                                    photo=f"downloads/{user.id}.jpg",
                                    caption=f"**❖ {user.first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                                )
                    except:
                        msg += f"**❖ {user.first_name[:25]}** ɪs ᴀғᴋ\n\n"
            elif (entity[j].type) == MessageEntityType.TEXT_MENTION:
                try:
                    user_id = entity[j].user.id
                    if user_id == replied_user_id:
                        j += 1
                        continue
                    first_name = entity[j].user.first_name
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_afk(user_id)
                if verifier:
                    try:
                        afktype = reasondb["type"]
                        timeafk = reasondb["time"]
                        data = reasondb["data"]
                        reasonafk = reasondb["reason"]
                        seenago = get_readable_time((int(time.time() - timeafk)))
                        if afktype == "text":
                            msg += f"**❖ {first_name[:25]}** is ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n"
                        if afktype == "text_reason":
                            msg += f"**❖ {first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n"
                        if afktype == "animation":
                            if str(reasonafk) == "None":
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**❖ {first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                                )
                            else:
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**❖ {first_name[:25]}** ɪs AFK sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                                )
                        if afktype == "photo":
                            if str(reasonafk) == "None":
                                send = await message.reply_photo(
                                    photo=f"downloads/{user_id}.jpg",
                                    caption=f"**❖ {first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                                )
                            else:
                                send = await message.reply_photo(
                                    photo=f"downloads/{user_id}.jpg",
                                    caption=f"**❖ {first_name[:25]}** ɪs ᴀғᴋ sɪɴᴄᴇ {seenago}\n\n● ʀᴇᴀsᴏɴ ➥ `{reasonafk}`\n\n", reply_markup=InlineKeyboardMarkup(EVAA),
                                )
                    except:
                        msg += f"**❖ {first_name[:25]}** ɪs ᴀғᴋ\n\n"
            j += 1
    if msg != "":
        try:
            send = await message.reply_text(msg, disable_web_page_preview=True)
        except:
            return

__mod_name__ = "ᴀғᴋ"

__help__ = """

⬤ /afk <reason> *➥* ᴍᴀʀᴋ ʏᴏᴜʀsᴇʟғ ᴀs ᴀғᴋ.
⬤ brb, !afk <reason> *➥* sᴀᴍᴇ ᴀs ᴛʜᴇ ᴀғᴋ ᴄᴏᴍᴍᴀɴᴅ.
"""

