from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
from AvishaRobot import pbot as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/avishaxbot?startgroup=true"),
    ],
]

@app.on_message(filters.command("day"))
def date_to_day_command(client: Client, message: Message):
    try:
        
        command_parts = message.text.split(" ", 1)
        if len(command_parts) == 2:
            input_date = command_parts[1].strip()
            date_object = datetime.strptime(input_date, "%Y-%m-%d")
            day_of_week = date_object.strftime("%A")

            
            message.reply_text(f"⬤ ᴛʜᴇ ᴅᴀʏ ᴏғ ᴛʜɪs ᴅᴀᴛᴇ ➣ {input_date} ɪs ➥ {day_of_week}.", reply_markup=InlineKeyboardMarkup(EVAA),)


        else:
            message.reply_text("⬤ Please provide a valid date in the format ➥ `/day 2006-09-19` ")

    except ValueError as e:
        message.reply_text(f"⬤ Error ➥ {str(e)}")
      
