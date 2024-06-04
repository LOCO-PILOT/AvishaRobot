
import requests
from AvishaRobot.events import register
from AvishaRobot import telethn
from AvishaRobot import SUPPORT_CHAT
from bs4 import BeautifulSoup

@register(pattern='/watchorder')
async def watchorder(event):
	animename = event.message.message.replace(event.text.split(' ')[0], '')
	if len(animename) <= 1:
		await event.reply(f"⬤ ᴡᴀᴛᴄʜ ᴀɴɪᴍᴇ ➥ '/watchorder anime name' ")
		return
	try:
		res = requests.get(f'https://chiaki.site/?/tools/autocomplete_series&term={animename}').json()
		data = None
		id_ = res[0]['id']
		res_ = requests.get(f'https://chiaki.site/?/tools/watch_order/id/{id_}').text
		soup = BeautifulSoup(res_ , 'html.parser')
		anime_names = soup.find_all('span' , class_='wo_title')
		for x in anime_names:
			data = f"{data}\n{x.text}" if data else x.text
		await telethn.send_message(event.chat_id, f'⬤ ᴡᴀᴛᴄʜ ᴏʀᴅᴇʀ ᴏғ <b>`{animename}` ⏤͟͟͞͞★</b> \n\n<tt>{data}</tt>',parse_mode='html', reply_to=event.id)
	except Exception as e:
		await event.reply(f'⬤ *ᴇʀʀᴏʀ* ➥ ᴄᴏɴᴛᴀᴄᴛ @{SUPPORT_CHAT}.\n\n⬤ ᴇʀʀᴏʀ ➥ `{e}')
		return

