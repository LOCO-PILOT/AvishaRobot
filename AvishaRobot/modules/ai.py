import requests

from pyrogram import filters, Client
from pyrogram.types import Message, InputMediaPhoto
from AvishaRobot import pbot as app
from pyrogram.errors import MediaCaptionTooLong

api_url_gpt = "https://nandha-api.onrender.com/ai/gpt"
api_url_bard = "https://nandha-api.onrender.com/ai/bard"

def fetch_data(api_url: str, query: str) -> tuple:
    try:
        response = requests.get(f"{api_url}/{query}")
        response.raise_for_status()
        data = response.json()
        return data.get("content", "⬤ ɴᴏ ʀᴇsᴘᴏɴsᴇ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ."), data.get("images", False)
    except requests.exceptions.RequestException as e:
        return None, f"⬤ ʀᴇǫᴜᴇsᴛ ᴇʀʀᴏʀ ➥ {e}"
    except Exception as e:
        return None, f"⬤ ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ➥ {str(e)}"

@app.on_message(filters.command(["ask"]))
async def chatgpt(_, message):
    if len(message.command) < 2:
        return await message.reply_text("⬤ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇʀʏ.")

    query = " ".join(message.command[1:])    
    txt = await message.reply_text("⬤ ᴡᴀɪᴛ ᴘᴀᴛɪᴇɴᴛʟʏ, ʀᴇǫᴜᴇsᴛɪɴɢ ᴛᴏ ᴀᴘɪ...")
    await txt.edit("💭")
    api_response, error_message = fetch_data(api_url_gpt, query)
    await txt.edit(api_response or error_message)





@app.on_message(filters.command(["bard"]))
async def bard(_, message):
    chat_id = message.chat.id
    message_id = message.id
    
    if len(message.command) < 2:
        return await message.reply_text("⬤ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇʀʏ.")

    query = " ".join(message.command[1:])
    txt = await message.reply_text("⬤ ᴡᴀɪᴛ ᴘᴀᴛɪᴇɴᴛʟʏ, ʀᴇǫᴜᴇsᴛɪɴɢ ᴛᴏ ᴀᴘɪ...")
    await txt.edit("💭")
    
    api_response, images = fetch_data(api_url_bard, query)

    medias = []
    bard = str(api_response)
    try:
       photo_url = images[-1]
    except:
        pass
    
    
    if images:
        if len(images) > 1:
            for url in images:
                medias.append(InputMediaPhoto(media=url, caption=None))
                        
            medias[-1] = InputMediaPhoto(media=photo_url, caption=bard)
            
            try:
                await app.send_media_group(chat_id=chat_id, media=medias, reply_to_message_id=message_id)
                return await txt.delete()
            except Exception as e:
                return await txt.edit(str(e))
        elif len(images) < 2:
            image_url = images[0]
            try:
                await message.reply_photo(photo=image_url, caption=bard)
                return await txt.delete()
            except MediaCaptionTooLong:
                return await txt.edit(bard)
            except Exception as e:
                return await txt.edit(str(e))
        else:
            return await txt.edit('⬤ sᴏᴍᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ')
    else:
        try:
            return await txt.edit(bard)
        except Exception as e:
            return await txt.edit(str(e))


__mod_name__ = "ᴀɪ-ɢᴘᴛ"

__help__ = """

 ⬤ /ask *➥* ʀᴇᴘʟʏ ᴛo ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ 💭
 ⬤ /gpt *➥* ʀᴇᴘʟʏ ᴛo ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ 💭
 ⬤ /bard *➥* ʀᴇᴘʟʏ ᴛo ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ 💭
 """
