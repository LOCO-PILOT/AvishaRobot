import httpx, base64
from pyrogram import filters
from AvishaRobot import pbot as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/avishaxbot?startgroup=true"),
    ],
]

@app.on_message(filters.command("upscale"))
async def upscale_image(client, message):
    try:
        # Check if the replied message contains a photo
        if message.reply_to_message and message.reply_to_message.photo:
            # Send a message indicating upscaling is in progress
            progress_msg = await message.reply_text(
                "🎆"
            )

            # Access the image file_id from the replied message
            image = message.reply_to_message.photo.file_id
            file_path = await client.download_media(image)

            with open(file_path, "rb") as image_file:
                f = image_file.read()

            b = base64.b64encode(f).decode("utf-8")

            async with httpx.AsyncClient() as http_client:
                response = await http_client.post(
                    "https://api.qewertyy.me/upscale",
                    data={"image_data": b},
                    timeout=None,
                )

            # Save the upscaled image
            upscaled_file_path = "upscaled_image.png"
            with open(upscaled_file_path, "wb") as output_file:
                output_file.write(response.content)

            # Delete the progress message
            await progress_msg.delete()

            # Send the upscaled image as a PNG file
            await client.send_document(
                message.chat.id,
                document=upscaled_file_path,
                caption=f"⬤ **ᴜᴘsᴄᴀʟᴇᴅ ɪᴍᴀɢᴇ ʙʏ ➥** [๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐](https://t.me/Avishaxbot)", reply_markup=InlineKeyboardMarkup(EVAA),
            )
        else:
            await message.reply_text("⬤ ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ɪᴛ.")

    except Exception as e:
        print(f"⬤ ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ➥ {e}")
        await message.reply_text("⬤ ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ᴛʜᴇ ɪᴍᴀɢᴇ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.")
        # You may want to handle the error more gracefully here
      
