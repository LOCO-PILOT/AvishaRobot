import os
import cv2
from io import BytesIO
from AvishaRobot import dispatcher
from AvishaRobot.modules.disable import DisableAbleCommandHandler
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, run_async

#####$

def sketch(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id
    message = update.effective_message
    try:
        if message.reply_to_message and message.reply_to_message.photo:
                file_id = message.reply_to_message.photo[-1].file_id
                newFile = context.bot.get_file(file_id)
                newFile.download("getSketchfile.png")
                #reading image
                image = cv2.imread("getSketchfile.png")
                #converting BGR image to grayscale
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                #image inversion
                inverted_image = 255 - gray_image

                blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
                inverted_blurred = 255 - blurred
                pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=120.0)


                filename = 'my_sketch.png'
                cv2.imwrite(filename, pencil_sketch)
                ofile = open(filename, "rb")
                bot.send_photo(chat_id, ofile)
                if os.path.exists("getSketchfile.png"):
                    os.remove("getSketchfile.png")
                if os.path.exists(filename):
                    os.remove(filename)

        else:
            update.effective_message.reply_text(
                "⬤ ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴀ sᴋᴇᴛᴄʜ.",
            )

    except Exception as e:
      message.reply_text(f'⬤ ᴇʀʀᴏʀ, ʀᴇᴘᴏʀᴛ @the_friendz ➥ {e}')



__help__ = """

 ⬤ /sketch *➥*  ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ɪᴍᴀɢᴇ sᴋᴇᴛᴄʜ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴘɪᴄᴛᴜʀᴇ.
 """

__mod_name__ = "sᴋᴇᴛᴄʜ"

SKETCH_HANDLER = DisableAbleCommandHandler("sketch", sketch, run_async=True)
dispatcher.add_handler(SKETCH_HANDLER)
