import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
#from collections import Counter

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    string = "/start is called"
    print(string)
    update.message.reply_text(string)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def word_count(update, context):
    user_text = update.message.text 
    word_list = user_text.split()
    word_list.remove("/wordcount")
    word_number = len(word_list)

    print(f"The number of words is: {word_number}")
    update.message.reply_text(f"The number of words is: {word_number}")

def full_moon(update, context):
    user_text = update.message.text
    date = user_text.split()[-1]
    print(ephem.next_full_moon(date))
    update.message.reply_text(ephem.next_full_moon(date))

city_list = ["moscow", "warsaw", "mellington", "new york"]

def cities(update, context):
    user_text = update.message.text
    city = user_text.split()
    city.remove("/cities")
    # Handle cities with whitespaces in it
    a = " "
    a = a.join(city).lower()
    print(a)

    if a in city_list:
        city_list.remove(a)
        last_letter = a[-1]
        for i in city_list:
            if i.startswith(last_letter):
                print(i)
                city_list.remove(i)
    else:
        print(a)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("next_full_moon", full_moon))
    dp.add_handler(CommandHandler("cities", cities))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot has started")

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()