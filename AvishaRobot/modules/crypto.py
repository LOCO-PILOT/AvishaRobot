from AvishaRobot.core.sections import section
import requests
from AvishaRobot import dispatcher
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

def crypto(update: Update, context: CallbackContext):
    message = update.effective_message
    args = context.args
    if len(args) == 0:
        return message.reply_text("/crypto [currency]")

    currency = message.text.split(None, 1)[1].lower()

    buttons = [
        [
            InlineKeyboardButton(text = "ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴜʀʀᴇɴᴄɪᴇs", url ="https://plotcryptoprice.herokuapp.com"),
        ],
    ]

    try:
        url = f'https://x.wazirx.com/wazirx-falcon/api/v2.0/crypto_rates'
        result = requests.get(url).json()
    except Exception:
        return message.reply_text("⬤ [ᴇʀʀᴏʀ] ➥ sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.")

    if currency not in result:
        return update.effective_message.reply_text(
            "⬤ [ᴇʀʀᴏʀ] ➥ ɪɴᴠᴀʟɪᴅ ᴄᴜʀʀᴇɴᴄʏ",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    body = {i.upper(): j for i, j in result.get(currency).items()}

    text = section(
        "⬤ ᴄᴜʀʀᴇɴᴛ ᴄʀʏᴘᴛᴏ ʀᴀᴛᴇs ғᴏʀ \n" + currency.upper(),
        body,
    )
    update.effective_message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), parse_mode=ParseMode.MARKDOWN)

CRYPTO_HANDLER = CommandHandler("crypto", crypto, run_async=True)

dispatcher.add_handler(CRYPTO_HANDLER)

__handlers__ = [
    CRYPTO_HANDLER
]


__mod_name__ = "ᴄʀʏᴘᴛᴏ"

__help__ = """

 ⬤ `/crypto` [ᴄᴜʀʀᴇɴᴄʏ] ➥ ɢᴇᴛ ʀᴇᴀʟ ᴛɪᴍᴇ ᴠᴀʟᴜᴇ ғʀᴏᴍ ᴄᴜʀʀᴇɴᴄʏ ɢɪᴠᴇɴ.
"""
