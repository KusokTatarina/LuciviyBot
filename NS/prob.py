from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '6511744553:AAE85JGv_6SqPeq2OtjT78arhk87GEpHhDs'

# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# admin_ids: list[int] = [1013293350]

# class IsAdmin(BaseFilter):
#     def __init__(self, admin_ids: list[int]) -> None:
#         self.admin_ids = admin_ids
#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in self.admin_ids
    
class NumberInMessage(BaseFilter):
    async def __call__(self, message: Message):
        numbers = []
        for word in message.text.split():
            norm_word = word.replace('.', '').replace(',', '').strip()
            if norm_word.isdigit():
                numbers.append(int(norm_word))
        if numbers: 
            return {'numbers': numbers}
        return False
        
@dp.message(F.text.lower().startswith('найди числа'), NumberInMessage())
async def if_numbers(message: Message, numbers: list[int]):
    await message.answer(text=f'Нашел: {", ".join(str(num) for num in numbers)}')

@dp.message(F.text.lower().starwish('найди числа'))
async def not_numbers(message: Message):
    await message.answer(text='Ничего не нашёл')

# @dp.message(IsAdmin(admin_ids))
# async def answer_if_admins_update(message: Message):
#     await message.answer(text='you administrator')

# @dp.message()
# async def answer_if_no_admins_update(message: Message):
#     await message.answer(text='No admins found')

if __name__ == '__main__':
    dp.run_polling(bot)