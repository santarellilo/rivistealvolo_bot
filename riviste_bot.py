import requests
import telepot
from bs4 import BeautifulSoup

def ottieniLink(link):
	r = requests.get(link)
	soup = BeautifulSoup(r.content, "html.parser").find('iframe').get('src')
	newLink = soup[34:-14]
	return newLink

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == 'text':
		name = msg["from"]["first_name"]
        ricerca = msg['text']
        if ricerca == '/help':
        	bot.sendMessage(chat_id, 'Scrivi cosa vuoi scaricare')
        else:
        	cerca(ricerca, chat_id)

TOKEN = '505211509:AAG7Mi4Cw8ZGYYCDJ7U1lFvcP2cNVf3qc6c'

bot = telepot.Bot(TOKEN)
bot.deleteWebhook()
bot.message_loop(on_chat_message)

def cerca(query, chat_id):
	page_no = 1
	giornali = {}
	while page_no < 6:
		payload = {
			'op':'user_public',
			'load':'files',
			'page':page_no,
			'fld_id':'1534',
			'usr_login':'magazine'
		}
		r = requests.post(
			url='https://nodefiles.com/users/magazine/1534/RIVISTE',
			data=payload,
			headers={
				'X-Requested-With': 'XMLHttpRequest'
			}
		)
		s = BeautifulSoup(r.content, "html.parser")
		if not s.a:
			break

		elementi = s.find_all('a', href=True)
		for el in elementi:
			giornali[el.text]=el.get('href')

		page_no += 1 

	risultati = {}
	n = 0
	for gio in giornali:
		if query.lower() in gio.lower():
			risultati[gio]=giornali[gio]

	print 'Ecco cosa ho trovato.. '

	for ris in risultati:
		bot.sendMessage(chat_id, ris)
		bot.sendMessage(chat_id, ottieniLink(risultati[ris]))

print 'Listening .. '

import time 
while 1:
	time.sleep(10)