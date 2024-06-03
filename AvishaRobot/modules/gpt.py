import requests
from AvishaRobot import telethn as tbot
from AvishaRobot.events import register

GPT_API_URL = "https://chatgpt.apinepdev.workers.dev"


@register(pattern="^/gpt (.*)")
async def chat_gpt(event):
    if event.fwd_from:
        return

    query = event.pattern_match.group(1)

    if query:
        # Send "Please wait" message
        processing_message = await event.reply("💭")

        try:
            # Make a request to GPT API
            response = requests.get(f"{GPT_API_URL}/?question={query}")

            if response.status_code == 200:
                # Extract the answer from the API response
                result = response.json()

                # Check if "join" key is present and remove it
                if "join" in result:
                    del result["join"]

                # Add signature to the answer
                answer = result.get("answer", "⬤ ɴᴏ ᴀɴsᴡᴇʀ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ᴄʜᴀᴛ ᴀɪ.")
                signature = "\n\n❖ ᴀɴsᴡᴇʀɪɴɢ ʙʏ ➥ [๛ᴀ ᴠ ɪ s ʜ ᴀ ♡゙](https://t.me/the_friendz)"
                reply_message = answer + signature

                # Edit the "Please wait" message with the final answer
                await processing_message.edit(reply_message)
            else:
                # If there's an error with the API, inform the user
                await processing_message.edit("⬤ ᴇʀʀᴏʀ ᴄᴏᴍᴍᴜɴɪᴄᴀᴛɪɴɢ ᴡɪᴛʜ sᴏʟᴠᴇ ᴀᴘɪ.")
        except requests.exceptions.RequestException as e:
            # Handle network-related errors
            await processing_message.edit(f"⬤ ᴇʀʀᴏʀ ➥ {str(e)}. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.")
        except Exception as e:
            # Handle unexpected errors
            await processing_message.edit(f"⬤ ᴜɴᴇxᴘᴇᴄᴛᴇᴅ ᴇʀʀᴏʀ ➥ {str(e)}. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.")
    else:
        # Provide information about the correct command format
        await event.reply("⬤ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇsᴛɪᴏɴ ᴀғᴛᴇʀ /solve ᴄᴏᴍᴍᴀɴᴅ.\n\n● ғᴏʀ ᴇxᴀᴍᴘʟᴇ ➥ /gpt ᴡʜᴀᴛ ɪs ᴛʜᴇ ᴠᴀʟᴜᴇ ᴏғ sɪɴ 60° ?")


