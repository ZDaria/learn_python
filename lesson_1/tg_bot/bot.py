from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import logging
import ephem
import datetime


logging.basicConfig(filename=config.filename, level=logging.INFO)
PROXY = {'proxy_url': config.proxy, config.url: {'username': config.user,
                                                 'password': config.pwd}}


def talk_to_me(update):
    user_text = update.message.text.split()
    logging.info(f"We have got msg from user {user_text}")
    if user_text[0] == "/planet":
        logging.info(f"Getting {user_text[0]} info ... ")
        planet_location = get_planet_info(user_text[1])
        logging.info(f"Response to the user: {planet_location[1]}")
        update.message.reply_text(planet_location[1])
    else:
        logging.info(f"Print user's msg one more time...")
        update.message.reply_text(user_text)


def greet_user(update):
    update.message.reply_text("Привет пользователь! Ты вызвал команду /start")


def get_planet_info(planet_name):
    logging.info(f"Today date: {datetime.date.today()}")
    planet_info = getattr(ephem, planet_name)(str(datetime.date.today()))
    logging.info(f"We have got planet info: {planet_info}")
    return ephem.constellation(planet_info)


def main():
    my_bot = Updater(config.my_key, use_context=True)
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Starting bot")
    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()
