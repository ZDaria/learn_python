from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import logging
import ephem
import datetime
from collections import Counter


logging.basicConfig(filename=config.filename, level=logging.INFO)
PROXY = {'proxy_url': config.proxy, config.url: {'username': config.user, 'password': config.pwd}}


def talk_to_me(update, context):
    user_text = update.message.text.split()
    if user_text[0] == "/planet":
        planet = ephem.user_text[1](str(datetime.date.today()))
        planet_location = ephem.constellation(planet)
        update.message.reply_text(planet_location)
    else:
        update.message.reply_text(user_text)


def greet_user(update, context):
    update.message.reply_text("Привет пользователь! Ты вызвал команду /start")


def get_planet(update, context):
    planet = ephem.Mars(str(datetime.date.today()))
    const = ephem.constellation(planet)
    update.message.reply_text(const)


def main():
    my_bot = Updater(config.my_key, use_context=True)
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Starting bot")
    my_bot.start_polling()
    my_bot.idle()


main()
