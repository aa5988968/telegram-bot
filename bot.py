import telebot

TOKEN = "8272488488:AAGQPXUrKIU5iGk571s2XY2pQgZSja4s7KY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "স্বাগতম! আপনার বট চালু হয়েছে ✅")

bot.infinity_polling()
