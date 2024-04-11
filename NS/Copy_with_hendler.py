from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '6850289793:AAGh_f5obILLX0qd5tecl5BIkBqZC-Parpw'
# BOT_TOKEN ='5788580379:AAExLisvcziFci2k2zoZ-XEtCwqwZow3YPc'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



# Этот хэндлер будет срабатывать на команду "/start"
# @dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')




# Этот хэндлер будет срабатывать на команду "/help"
# @dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )



# Этот хэндлер будет срабатывать на отправку стикеров
async def send_sticers_echo(message: Message):
    await message.answer_sticker(message.sticker.file_id)



# dp.message.register(F.content_type == ContentType.PHOTO)
async def send_photo_ecgo(message: Message):
    
    await message.answer_photo(message.photo[0].file_id)




# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
# @dp.message()
async def send_echo(message: Message):
    await message.answer(text=message.text)




dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_ecgo, F.photo)
dp.message.register(send_sticers_echo, F.sticker)
# dp.message.register(send_sticker_echo, content_types=['sticker'])
dp.message.register(send_echo)



if __name__ == '__main__':
    dp.run_polling(bot)










    