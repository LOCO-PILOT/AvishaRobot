import logging
import random
import requests
from telethon import events
from AvishaRobot import telethn as meow

logging.basicConfig(level=logging.DEBUG)

MemesReddit = [
    "Animemes",
    "lostpause",
    "LoliMemes",
    "cleananimemes",
    "animememes",
    "goodanimemes",
    "AnimeFunny",
    "dankmemes",
    "teenagers",
    "shitposting",
    "Hornyjail",
    "wholesomememes",
    "cursedcomments",
]

@meow.on(events.NewMessage(pattern="^/memes"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = f"https://meme-api.com/gimme/{memereddit}"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/dank"))
async def mimi(event):
    try:
        random.choice(MemesReddit)
        meme_link = "https://meme-api.com/gimme/dankmemes"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/lolimeme"))
async def mimi(event):
    try:
        random.choice(MemesReddit)
        meme_link = "https://meme-api.com/gimme/LoliMemes"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/hjail"))
async def mimi(event):
    try:
        random.choice(MemesReddit)
        meme_link = "https://meme-api.com/gimme/Hornyjail"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/wmeme"))
async def mimi(event):
    try:
        random.choice(MemesReddit)
        meme_link = "https://meme-api.com/gimme/wholesomememes"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/pewds"))
async def mimi(event):
    try:
        random.choice(MemesReddit)
        meme_link = "https://meme-api.com/gimme/PewdiepieSubmissions"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/hmeme"))
async def mimi(event):
    try:
        random.choice(MemesReddit)
        meme_link = "https://meme-api.com/gimme/hornyresistance"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/teen"))
async def mimi(event):
    try:
        random.choice(MemesReddit)
        meme_link = "https://meme-api.com/gimme/teenagers"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/fbi"))
async def mimi(event):
    try:
        random.choice(MemesReddit)
        meme_link = "https://meme-api.com/gimme/FBI_Memes"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/shitposting"))
async def mimi(event):
    try:
        random.choice(MemesReddit)
        meme_link = "https://meme-api.com/gimme/shitposting"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/cursed"))
async def mimi(event):
    try:
        random.choice(MemesReddit)
        meme_link = "https://meme-api.com/gimme/cursedcomments"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])

    except Exception as e:
        print(e)


__help__ = """

⬤ /memes ➥ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴍɪxᴇᴅ ᴍᴇᴍᴇs
⬤ /wmeme ➥ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴡʜᴏʟᴇsᴏᴍᴇ ᴍᴇᴍᴇs
⬤ /dank ➥ ᴘʀᴏᴠɪᴅᴇs ᴅᴀɴᴋ ᴍᴇᴍᴇs
⬤ /cursed ➥ ᴄᴜʀsᴇᴅ ᴍᴇᴍᴇs
⬤ /shitposting ➥ ʀᴀɴᴅᴏᴍ sʜɪᴛᴘᴏsᴛs
⬤ /fbi ➥ ғʙɪ ᴍᴇᴍᴇs
⬤ /teen ➥ ᴛᴇᴇɴᴀɢᴇʀs ᴍᴇᴍᴇ
⬤ /hmeme ➥ ʜᴏʀɴʏ ᴍᴇᴍᴇs
⬤ /pewds ➥ ᴘᴇᴡᴅɪᴇᴘɪᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ
⬤ /hjail ➥ ᴏɴɪᴄʜᴀɴ ᴀʀʀᴇsᴛᴇᴅ
⬤ /lolimeme ➥ ʟᴏʟɪ ᴍᴇᴍᴇs
"""

__mod_name__ = "ᴍᴇᴍᴇs"

