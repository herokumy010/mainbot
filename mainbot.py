import telebot
import random
bot = telebot.TeleBot('7122310145:AAFnWK7uEIrdj3h8r28exZ-zcf6xTYq_2U0')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحبا! يمكنك استخدام /generate لإنشاء ايميل جديد.")

@bot.message_handler(commands=['generate'])
def generate_email(message):
    modca = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8)) + '@gmail.com'
    bot.reply_to(message, f"الايميل الجديد هو: {modca}")
    
bot.polling()