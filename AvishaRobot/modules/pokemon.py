from pyrogram import Client, filters
import requests
from AvishaRobot import pbot as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatAction, ParseMode

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/avishaxbot?startgroup=true"),
    ],
]

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"


@app.on_message(filters.command("pokemon"))
async def CutexMusic(client, message):
    # copy pasters u can copy paste but give credits to me and pokeapi.co and Pokemondb.net
    command_parts = message.text.split(None, 1)
    if len(command_parts) < 2:
        await message.reply_text("⬤ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴍᴇ ᴀ ᴘᴏᴋᴇᴍᴏɴ ɴᴀᴍᴇ.")
        return
    pokemon_name = command_parts[1].strip()
    pokemon_url = f"{POKEAPI_BASE_URL}pokemon/{pokemon_name.lower()}"

    try:
        response = requests.get(pokemon_url)
        data = response.json()

        # Extract krlo 
        name = data["name"].capitalize()
        abilities = ", ".join([ability["ability"]["name"] for ability in data["abilities"]])
        stats = {stat["stat"]["name"].capitalize(): stat["base_stat"] for stat in data["stats"]}

        # response messssages
        response_message = f"❖ {name} ⏤͟͟͞͞★\n\n"
        response_message += f"● ᴀʙɪʟɪᴛɪᴇs ➥ {abilities}\n\n"
        response_message += "❖ ᴘᴏᴋᴇᴍᴏɴ sᴛᴀᴛs ⏤͟͟͞͞★\n\n"
        for stat, value in stats.items():
            response_message += f"● {stat} ➥ {value}\n"

        poke_img_url = f"https://img.pokemondb.net/artwork/{pokemon_name.lower()}.jpg"

        # AHHHHH FINNALY DONE 
        await message.reply_photo(photo=poke_img_url, caption=response_message, reply_markup=InlineKeyboardMarkup(EVAA), parse_mode=ParseMode.MARKDOWN)

    except requests.HTTPError as e:
        await message.reply_text(f"⬤ ᴇʀʀᴏʀ ➥ {e}")
    except requests.RequestException as e:
           # ITTU SA ERROR 
        await message.reply_text("⬤ ᴇʀʀᴏʀ ➥ @The_Friendz ♥︎")
    except KeyError:
           # I THIKNK YE NHI CHIYE 
        await message.reply_text("⬤ ᴘᴏᴋᴇᴍᴏɴ ᴡᴀs ɴᴏᴛ ғᴏᴜɴᴅ.")


#####

__mod_name__ = "ᴘᴏᴋᴇᴅᴇx"

__help__ = """

 ⬤ /pokemon ➥ sᴇᴀʀᴄʜ ᴘᴏᴋɪᴍᴀɴ ᴄʜᴀʀᴀᴄᴛᴇʀ.
 """
