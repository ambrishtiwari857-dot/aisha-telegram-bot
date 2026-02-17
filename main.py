import telebot

BOT_TOKEN = "8261717850:AAEqBR6h3gNrF2deXgIjbx8hJpEM6GpaOyQ"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "Hello from Aisha 💕")

bot.infinity_polling()
