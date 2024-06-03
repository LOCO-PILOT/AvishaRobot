from pyrogram import Client, filters
import requests
from io import BytesIO
from AvishaRobot import pbot as app

def get_random_picture():
    response = requests.get('https://source.unsplash.com/random')
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        return None  

@app.on_message(filters.command("randompic"))
def pic(client, message):
    random_pic = get_random_picture()
    if random_pic:
        message.reply_photo(random_pic)
    else:
        message.reply("⬤ Sorry, I couldn't get a random picture at the moment. 😔")

  
