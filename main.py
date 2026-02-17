import os
import telebot
import time

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda m: True)
def reply(message):
    bot.reply_to(message, "Heyy 💖 I'm alive and running!")

while True:
    try:
        print("Bot started...")
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)