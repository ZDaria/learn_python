from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import logging
import ephem
import datetime


logging.basicConfig(filename=config.filename, level=logging.INFO)
PROXY = {'proxy_url': config.proxy, config.url: {'username': config.user, 'password': config.pwd}}


def talk_to_me(update, context):
    user_text = update.message.text.split()
    print(user_text[0])
    if user_text[0] == "/planet":
        planet_location = get_planet_info(user_text[1])
        update.message.reply_text(planet_location[1])
    else:
        update.message.reply_text(user_text)


def greet_user(update, context):
    update.message.reply_text("Привет пользователь! Ты вызвал команду /start")


def get_planet_info(planet_name):
    planet_info = getattr(ephem, planet_name)(str(datetime.date.today()))
    return ephem.constellation(planet_info)


def main():
    my_bot = Updater(config.my_key, use_context=True)
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Starting bot")
    my_bot.start_polling()
    my_bot.idle()


main()
