import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from AvishaRobot import telethn as client

spam_chats = []

@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
@client.on(events.NewMessage(pattern="^/tagall ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "⬤ This command can be use in groups and channels."
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("⬤ Only admins can mention all.")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("⬤ Give me one argument.")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "⬤ ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ғᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs."
            )
    else:
        return await event.respond(
            "⬤ Reply to a message or give me some text to mention others."
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"☆ [{usr.first_name}](tg://user?id={usr.id})\n\n"
        if usrnum == 3:
            if mode == "text_on_cmd":
                txt = f"{msg}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(3)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("⬤ ᴛʜᴇʀᴇ ɪs ɴᴏ ᴘʀᴏᴄᴄᴇss ᴏɴ ɢᴏɪɴɢ..")
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("⬤ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")

    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("⬤ sᴛᴏᴘᴘᴇᴅ ᴍᴇɴᴛɪᴏɴ...♥︎")


__mod_name__ = "ᴛᴀɢɢᴇʀ"

__help__ = """

⬤ /tagall ᴏʀ /utag ➥ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
⬤ /cancel ➥ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.

⬤ /entag ➥ ᴇɴɢʟɪsʜ ᴛᴀɢ. || ● sᴛᴏᴘ ➣ /enstop
⬤ /lifetag ➥ ʟɪғᴇ ǫᴜᴏᴛᴇs ᴛᴀɢ. || ● sᴛᴏᴘ ➣ /lstop
⬤ /hitag ➥ ʜɪɴᴅɪ ᴛᴀɢ. || ● sᴛᴏᴘ ➣ /histop
⬤ /rtag ➥ ʀᴀɴᴅᴏᴍ ᴍᴇssᴀɢᴇ ᴛᴀɢ. || ● sᴛᴏᴘ ➣ /rstop
⬤ /stag ➥ sʜʏᴀʀɪ ᴛᴀɢ. || ● sᴛᴏᴘ ➣ /sstop
⬤ /bntag ➥ ʙᴀɴɢʟᴀ ᴛᴀɢ. || ● sᴛᴏᴘ ➣ /bnstop
⬤ /vctag ➥ ᴠᴄ ɪɴᴠɪᴛᴇ ᴛᴀɢ. || ● sᴛᴏᴘ ➣ /vstop
"""
      
