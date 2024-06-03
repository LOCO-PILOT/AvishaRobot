from faker import Faker

from faker.providers import internet
from telethon import events
from AvishaRobot import telethn as tbot

from pyrogram import filters
from AvishaRobot import pbot

@tbot.on(events.NewMessage(pattern="/fakegen$"))
async def hi(event):
    fake = Faker()
    print("💌")
    name = str(fake.name())
    fake.add_provider(internet)
    address = str(fake.address())
    ip = fake.ipv4_private()
    cc = fake.credit_card_full()
    email = fake.ascii_free_email()
    job = fake.job()
    android = fake.android_platform_token()
    pc = fake.chrome()
    await event.reply(
        f"<b>❖ ғᴀᴋᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b> ❖\n\n<b>● ɴᴀᴍᴇ ➥ </b><code>{name}</code>\n\n<b>● ᴀᴅᴅʀᴇss ➥ </b><code>{address}</code>\n\n<b>● ɪᴘ ᴀᴅᴅʀᴇss ➥ </b><code>{ip}</code>\n\n<b>● ᴄʀᴇᴅɪᴛ ᴄᴀʀᴅ ➥ </b><code>{cc}</code>\n\n<b>● ᴇᴍᴀɪʟ ɪᴅ ➥ </b><code>{email}</code>\n\n<b>● ᴊᴏʙ ➥ </b><code>{job}</code>\n\n<b>● ᴀɴᴅʀᴏɪᴅ ᴜsᴇʀ ᴀɢᴇɴᴛ ➥ </b><code>{android}</code>\n\n<b>● ᴘᴄ ᴜsᴇʀ ᴀɢᴇɴᴛ ➥ </b><code>{pc}</code>",
        parse_mode="HTML",
    )

@pbot.on_message(filters.command('picgen'))
async def picgen(_, message):
    img = "https://thispersondoesnotexist.com/image"
    text = f"⬤  ғᴀᴋᴇ ɪᴍᴀɢᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ."
    await message.reply_photo(photo=img, caption=text)




__mod_name__ = "ғᴀᴋᴇ-ɪɴғᴏ"

__help__ = """

⬤ `/fakegen` ➥ ɢᴇɴᴇʀᴀᴛᴇs ғᴀᴋᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
⬤ `/picgen` ➥ ɢᴇɴᴇʀᴀᴛᴇ ᴀ ғᴀᴋᴇ ᴘɪᴄ.
"""
