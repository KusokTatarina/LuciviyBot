from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ContentType
import random


bot_token = '6850289793:AAGh_f5obILLX0qd5tecl5BIkBqZC-Parpw'
bot = Bot(bot_token)

dp = Dispatcher()

attempts = 5


users ={}

def rand() -> int:
    return random.randint(1,100)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        'Привет!\nДавайте сыграем в игру "Угадай число"?\n\n'
        'Чтобы получить правила игры и список доступных '
        'команд - отправьте команду /help')
    if message.from_user.id not in users:
        users[message.from_user.id] = {'in game': False,
        'secret_number': None,
        'attempts': None,
        'total_games': 0,
        'wins': 0}

@dp.message(Command(commands='help'))
async def help(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
        f'а вам нужно его угадать\nУ вас есть {attempts} '
        f'попыток\n\nДоступные команды:\n/help - правила '
        f'игры и список команд\n/cancel - выйти из игры\n'
        f'/stat - посмотреть статистику\n\nДавай сыграем?')

@dp.message(Command(commands='stat'))
async def stat(message: Message):
    await message.answer(
        f'Всего в игре сыграно: {users[message.from_user.id]["total_games"]}\n Игр Выиграно: {users[message.from_user.id]["wins"]}'
    )

@dp.message(Command(commands='cancel'))
async def cancel(message: Message):
    if users[message.from_user.id]['in game']:
        users[message.from_user.id]['in game']=False
        await message.answer('Вы вышли из игры. Если захотите сыграть '
            'снова - напишите об этом')
    else:
        await message.answer(
            'А мы итак с вами не играем. '
            'Может, сыграем разок?'
        )

@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'игра',
                                'играть', 'хочу играть']))
async def play(message: Message):
    if not users[message.from_user.id]['in game']:
        users[message.from_user.id]['in game'] = True
        users[message.from_user.id]['attempts']=attempts
        users[message.from_user.id]['secret_number']= rand()
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
            'попробуй угадать!')
    else:
        await message.answer('Пока мы играем в игру я могу '
            'реагировать только на числа от 1 до 100 '
            'и команды /cancel и /stat')
        
@dp.message(F.text.lower().in_(['нет', 'не', 'не хочу', 'не буду']))       
async def leave(message: Message):
    if not users[message.from_user.id]['in game']:
        await message.answer(
            'Жаль :(\n\nЕсли захотите поиграть - просто '
            'напишите об этом'
        )
    else:
        await message.answer(
            'Мы же сейчас с вами играем. Присылайте, '
            'пожалуйста, числа от 1 до 100'
        )

@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text)<= 100)
async def send_number(message: Message):
    if users[message.from_user.id]['in game']:
        if int(message.text) == users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['in game'] = False
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
            await message.answer(
                'Ура!!! Вы угадали число!\n\n'
                'Может, сыграем еще?'
            )
        elif int(message.text)> users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('Моё число меньше')
        elif int(message.text)< users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('Моё число больше')
        if users[message.from_user.id]['attempts'] == 0:
            users[message.from_user.id]['in game'] = False
            users[message.from_user.id]['total_games'] += 1
            await message.answer(
                f'К сожалению, у вас больше не осталось '
                f'попыток. Вы проиграли :(\n\nМое число '
                f'было {users[message.from_user.id]["secret_number"]}\n\nДавайте '
                f'сыграем еще?')
    else:
        await message.answer('Мы ещё не играем. Хотите сыграть?')

@dp.message()
async def all(message: Message):
    if users[message.from_user.id]['in game'] == False:
        await message.answer('Я умею только играть в игру')
    else:
        await message.answer('Присылай мне чилса от 1 до 100')

if __name__ == '__main__':
    dp.run_polling(bot)