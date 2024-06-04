from pyrogram import Client, enums, filters
import asyncio
from AvishaRobot import pbot as avisha
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.handlers import MessageHandler

#####
EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/avishaxbot?startgroup=true"),
    ],
]

####

@avisha.on_message(filters.command("dice"))
async def dice(bot, message):
    x=await bot.send_dice(message.chat.id)
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}", reply_markup=InlineKeyboardMarkup(EVAA) ,quote=True)
  
@avisha.on_message(filters.command("dart"))
async def dart(bot, message):
    x=await bot.send_dice(message.chat.id, "🎯")
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}", reply_markup=InlineKeyboardMarkup(EVAA),quote=True)

@avisha.on_message(filters.command("basket"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🏀")
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}",reply_markup=InlineKeyboardMarkup(EVAA), quote=True)
@avisha.on_message(filters.command("jackpot"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎰")
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}",reply_markup=InlineKeyboardMarkup(EVAA), quote=True)
@avisha.on_message(filters.command("ball"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎳")
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}",reply_markup=InlineKeyboardMarkup(EVAA), quote=True)
@avisha.on_message(filters.command("football"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "⚽")
    m=x.dice.value
    await message.reply_text(f"⬤ ʜᴇʏ ʙᴀʙʏ ➥ {message.from_user.mention}\n⬤ ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➥ {m}",reply_markup=InlineKeyboardMarkup(EVAA), quote=True)

#####

__help__ = """

⬤ /dice ➥ ᴅɪᴄᴇ ɢᴀᴍᴇ  🎲
⬤ /dart ➥ ᴅᴀʀᴛ ɢᴀᴍᴇ  🎯
⬤ /basket ➥ ʙᴀsᴋᴇᴛ ʙᴀʟʟ ɢᴀᴍᴇ  🏀
⬤ /ball ➥ ʙᴏᴡʟɪɴɢ ʙᴀʟʟ ɢᴀᴍᴇ  🎳
⬤ /football ➥ ғᴏᴏᴛʙᴀʟʟ ɢᴀᴍᴇ  ⚽
⬤ /jackpot ➥ sᴘɪɴ sʟᴏᴛ ᴍᴀᴄʜɪɴᴇ ɢᴀᴍᴇ  🎰
⬤ /truth ➥ sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
⬤ /dare ➥ sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.
 """

__mod_name__ = "ɢᴀᴍᴇ"
