#!/usr/bin/python

#This script is independet of lib or python version (tested on python 2.7 and 3.5)
#pip3 install python-telegram-bot --upgrade

import telegram
import sys
import config

my_node = sys.argv[1]
their_node = sys.argv[2]

status = "ALLSTAR ALERT: Node " + str(their_node) + " disconnected from " + str(my_node)

def send(msg, chat_id=config.my_chat_id, token=config.my_token):
	"""
	Send a mensage to a telegram user specified on chatId
	chat_id must be a number!
	"""
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)

send(status)
