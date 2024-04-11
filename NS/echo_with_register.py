from aiogram import Bot, Dispatcher
# Из aiogram.filters импортируем класс Command, чтобы фильтровать апдейты по наличию в них команд,
# то есть сочетаний символов, начинающихся со знака "/"
from aiogram.filters import Command
# Из  aiogram.types импортируем класс Message. Апдейты этого типа мы будем ловить эхо-ботом
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather 
BOT_TOKEN = '6850289793:AAGh_f5obILLX0qd5tecl5BIkBqZC-Parpw' 

# Создаем объекты бота и диспетчера 
bot = Bot(token=BOT_TOKEN) 
dp = Dispatcher()


# # Без декораторов
# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на отправку фото
async def send_photo_echo(message: Message):
    # Чтобы получить фото с самым большим разрешением можно обратиться к полю photo по индексу [-1],
    # а с самым маленьким, соответственно, [0]
    await message.answer_photo(message.photo[0].file_id)


# Этот хэндлер будет срабатывать на отправку видео
async def send_video_echo(message: Message):
    await message.answer_video(message.video.file_id)


# Этот хэндлер будет срабатывать на отправку видео сообщений
async def send_video_note_echo(message: Message):
    await message.answer_video_note(message.video_note.file_id)


# Этот хэндлер будет срабатывать на отправку стикеров
async def send_sticker_echo(message: Message):
    await message.answer_sticker(message.sticker.file_id)


# Этот хэндлер будет срабатывать на отправку аудио файлов
async def send_audio_echo(message: Message):
    await message.answer_audio(message.audio.file_id)


# Этот хэндлер будет срабатывать на отправку голосовых сообщений
async def send_voice_echo(message: Message):
    await message.answer_voice(message.voice.file_id)


# Этот хэндлер будет срабатывать на отправку любых файлов
async def send_files(message: Message):
    await message.answer_document(message.document.file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(message.text)

# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
# отфильтровать апдейт по типу контента
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
# dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_video_note_echo, F.video_note)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_files, F.document)
dp.message.register(send_echo)


# Она запускает поллинг, то есть постоянный опрос сервера Telegram на наличие апдейтов для бота.
# В качестве аргумента в метод диспетчера run_polling нужно передать объект бота
if __name__ == '__main__':
    dp.run_polling(bot)