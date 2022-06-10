
from telebot import TeleBot
import requests as rq

token = "5384395652:AAF1TtpcwYMp1V9uMPShNkx9HOQKU414DfE"
bot = TeleBot(token)

@bot.message_handler(commands = ['start'])
def send(message):
    bot.reply_to(message, 'Hi, welcome to the NoeBot!')

@bot.message_handler(func=lambda message:True)
def send_message(message):
    if ('Medium' in message.text):
        resp = rq.get('http://127.0.0.1:8000/repoDatesMedium/%5B%27Ryan%20Fan%27%5D')
        print(resp.text[0]["title"])
        bot.reply_to(message, resp)

bot.polling()

