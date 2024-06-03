import requests
import random
import AvishaRobot.strings.animal_facts_string as animal_facts
from AvishaRobot import dispatcher
from telegram import Update
from AvishaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext


def animalfact(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(animal_facts.ANIMAL_FACTS))

def cats(update, context):
    msg = update.effective_message
    try:
        url = f'https://aws.random.cat/meow'
        result = requests.get(url).json()
        img = result['file']
        msg.reply_photo(photo=img)
    except:        
        url = f'https://aws.random.cat/meow'
        result = requests.get(url).json()
        img = result['file']
        msg.reply_photo(photo=img)

ANIMALFACT_HANDLER = DisableAbleCommandHandler("animalfacts", animalfact, run_async=True)
dispatcher.add_handler(ANIMALFACT_HANDLER)

__mod_name__ = "ᴀɴɪᴍᴀʟs"

__help__ = """

⬤ /animalfacts ➥ ᴛᴏ ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀɴɪᴍᴀʟ ғᴀᴄᴛs.
⬤ /goose ➥ sᴇɴᴅs ʀᴀɴᴅᴏᴍ ɢᴏᴏsᴇ ᴘɪᴄ.
⬤ /woof ➥ sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴡᴏᴏғ ᴘɪᴄ.
⬤ /lizard ➥ sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʟɪᴢᴀʀᴅ ɪᴍɢ.
"""
