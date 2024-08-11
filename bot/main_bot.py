from django.conf import settings
from telebot.async_telebot import AsyncTeleBot

from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)


@bot.message_handler(commands=['app'])
async def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('OpenWebApp', web_app=WebAppInfo(
        url='https://google.com/'
    )))
    await bot.send_message(message.chat.id, 'Hello', reply_markup=markup)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)
