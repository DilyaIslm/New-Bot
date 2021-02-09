import logging
from handlers import greet_user, guess_number, send_dog_picture, talk_to_me, user_coordinates
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

    
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("dog", send_dog_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать собачку)$'), send_dog_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
   main()    