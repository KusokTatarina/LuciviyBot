import json
from sqlalchemy import insert
from telebot import types, TeleBot
from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery
from database.database import create_tables, session
from database.models import User

bot = TeleBot(token='6511744553:AAE85JGv_6SqPeq2OtjT78arhk87GEpHhDs')

# create_tables()

@bot.message_handler(commands=['start'])
def startcomand(message: types.Message):
    # bot.send_message(message.chat.id,  f'{message}Привет, я робот долбаеб! Давай для начала познакомимся, как тебя зовут или как я могу к тебе обращаться?')
    bot.send_message(message.chat.id,  'Привет, я робот долбаеб! Давай для начала познакомимся, как тебя зовут или как я могу к тебе обращаться?')


@bot.message_handler(content_types=['text'])
def get(message: types.Message):
    global user_name
    global user_id
    user_name = str(message.text)
    user_id = message.chat.id
    print(user_name, message.chat.id)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Да', callback_data='yes'))
    markup.add(types.InlineKeyboardButton('Нет', callback_data='no'))
    bot.reply_to(message, f'Я правильно понял, что тебя зовут {user_name}', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback: CallbackQuery):
    # print(json.dumps(callback.json, indent=4, ensure_ascii=False))
    if callback.data == 'yes':
        with session() as sess:
            add = insert(User).values(user_id=user_id, name=user_name)
            sess.execute(add)
            sess.commit()
            bot.reply_to(callback.message, f'Очень приятно познакомится {user_name}')
    elif callback.data == 'no':
        bot.reply_to(callback.message, 'Ты лох')

# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'yes':
#         with session() as sess:
#             add = insert(User).values(user_id=user_id, name=user_name)
#             sess.execute(add)
#             sess.commit()
#             bot.reply_to(callback, f'Очень приятно познакомится {user_name}')
#     elif callback.data == 'no':
#         bot.reply_to(callback.message, 'Ты лох')

bot.polling(none_stop=True)