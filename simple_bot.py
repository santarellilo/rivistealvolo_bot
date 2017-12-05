import telepot

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == 'text':
		name = msg["from"]["first_name"]
        txt = msg['text']
        bot.sendMessage(chat_id, 'ciao %s, sono un bot molto stupido!' %name)
        bot.sendMessage(chat_id, 'ho ricevuto questo: %s' %txt)

TOKEN = '489953825:AAEYT3jAts7wqyiE5N6TBTsXozKY9J_VtLA'

bot = telepot.Bot(TOKEN)
bot.deleteWebhook()
bot.message_loop(on_chat_message)

print 'Listening .. '

import time 
while 1:
	time.sleep(10)