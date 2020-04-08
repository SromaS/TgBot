import telebot
from telebot.types import Message

import CoinmarketParser
from CoinmarketParser import base_url

token = '###'
bot = telebot.TeleBot(token)
commands_list = ['/start', '/help', '/cryptomarket']


@bot.message_handler(commands=['start', 'help', 'cryptomarket'])
def answer(message: Message):
    if message.text == commands_list[0]:
        bot.send_message(message.chat.id, 'I greet you, traveler.')
    elif message.text == commands_list[1]:
        coms = ''
        for command in commands_list:
            coms += command + '\n'
        bot.send_message(message.chat.id,
                         f'I was made to help you. You can control me using different commands:\n{coms}')
    elif message.text == commands_list[2]:
        bot.send_message(message.chat.id,
                        'Top 10 currencies:' + '\n' + CoinmarketParser.coinMarket_parse(CoinmarketParser.get_html(base_url), 10))


@bot.message_handler(func=lambda message: True)
def unknown_message(message: Message):
    bot.send_message(message.chat.id, '''I'm sorry, I don't understand you. Look at the list of commands :)''')


bot.polling()
