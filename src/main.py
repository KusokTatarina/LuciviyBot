import asyncio
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery, InputMediaPhoto

from database.database import async_create_tables
from database.repository import UserRepository, FreeSketchRepository, CalculСostRepository, insert_data_in_free_scetch
from examples_works.examples_work import group_my_examples_work1, group_my_examples_work2
from myself.photo import group_my_photo
from keyboard.keyboard import * # keybord_for_sketch, keybord_size, keyboard_yes_or_no, keybord_skin, keybord_menu, keybord_body, keybord_hand, keybord_leg, keybord_torso, keybord_back, keybord_head, keybord_neck


bot = AsyncTeleBot(token='6511744553:AAE85JGv_6SqPeq2OtjT78arhk87GEpHhDs')



#Команда старт для начала работы бота
@bot.message_handler(commands=['start'])
async def startcomand(message: types.Message):
    user_name = await UserRepository.get_username(message.chat.id)
    if user_name:
        await bot.send_message(message.chat.id, f'Привет, {user_name}, рада снова тебя видеть.\nВыбери нужный пункт из меню:', reply_markup=keybord_menu())
    else:
        await bot.send_message(message.chat.id,  'Привет, я тату-бот Виктории, помогу тебе рассчитать стоимость желаемой тату и покажу свободные эскизы, которые можно нанести на кожу 🖤\n\nДля начала давай познакомимся. Как тебя зовут? 👻')

@bot.message_handler(commands=['menu'])
async def startcomand(message: types.Message):
    user_name = await UserRepository.get_username(message.chat.id)
    if user_name:
        await bot.send_message(message.chat.id, f'☠️Ты снова в главном меню.☠️', reply_markup=keybord_menu())
        
    else:
        await bot.send_message(message.chat.id, 'Привет, я тату-бот Виктории, помогу тебе рассчитать стоимость желаемой тату и покажу свободные эскизы, которые можно нанести на кожу 🖤\n\nДля начала давай познакомимся. Как тебя зовут? 👻')
        


#Получение имени и работа с обычным текстом
@bot.message_handler(content_types=['text'])
async def get(message: types.Message):
    if await UserRepository.check_register_user(message.chat.id):
        await bot.send_message(message.chat.id, f'{await UserRepository.get_username(message.chat.id)}, я могу выполнять только заложенные функции. Вот их список', reply_markup=keybord_menu())
    else:
        user_name = await UserRepository.add_user_or_update(message.chat.id, message.text)
        await bot.reply_to(message, f'Я правильно поняла, что тебя зовут {user_name}?', reply_markup=keyboard_yes_or_no())


@bot.callback_query_handler(func=lambda callback: True)
async def callback_message(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    #Проверка имени пользователем   
    if callback.data == 'yes':
        user_name = await UserRepository.get_username(chat_id)
        await UserRepository.register_user(chat_id)
        await bot.send_message(chat_id, f'Приятно познакомиться, {user_name}.\nВыбери нужный пункт из меню:', reply_markup=keybord_menu())
    elif callback.data == 'no':
        await bot.send_message(chat_id, 'Хорошо, давай попробуем еще раз.\nКак тебя зовут или как я могу к тебе обращаться?')

    #Обо мне
    elif callback.data == 'myself':
        await bot.send_media_group(chat_id, group_my_photo(),)
        await bot.send_message(chat_id, 'Свяжись со мной в любой удобной для тебя соц сети',reply_markup=keybord_myself())
    
    #Примеры моих работ
    elif callback.data == 'my_work':
        await bot.send_media_group(chat_id, group_my_examples_work1())
        await bot.send_media_group(chat_id, group_my_examples_work2())
        await bot.send_message(chat_id, 'Все эти работы были выполнены по моим эскизам',reply_markup=keybord_menu())

    #Часто задаваемые вопросы
    elif callback.data == 'question':
        await bot.send_message(chat_id, 'Здесь представлен перечень вопосов, на который я могу ответить',reply_markup=keybord_question())
        

    #Вопросы про сеанс
    elif callback.data == 'seans_question':
        pic2 = open(r"C:\Users\nicki\Desktop\LuciviyBOT\src\question\seans2.jpg", "rb")
        pic3 = open(r"C:\Users\nicki\Desktop\LuciviyBOT\src\question\seans3.jpg", "rb")
        media = [                               
                InputMediaPhoto(pic2),
                InputMediaPhoto(pic3),
                ]
        
        await bot.send_media_group(chat_id, media)
        await bot.send_message(chat_id, '🖤От идеи до реализации🖤\nКак подготовиться к сеансу и что будет происходить ✨',reply_markup=keyboard_end_question())


    #Вопросы про уход
    elif callback.data == 'uhod_question':
        pic1 = open(r"C:\Users\nicki\Desktop\LuciviyBOT\src\question\uhod.jpg", "rb")
        await bot.send_photo(chat_id, pic1, '🛁Уход за татуировкой🧴',reply_markup=keyboard_end_question())

    #Вопросы про противоопоказания
    elif callback.data == 'protivopokaz_question':
        pic1 = open(r"C:\Users\nicki\Desktop\LuciviyBOT\src\question\protiv.jpg", "rb")
        await bot.send_photo(chat_id, pic1, '❗️Кому нельзя делать татуировку ❗️',reply_markup=keyboard_end_question())


    #Вопросы про Предоплату
    elif callback.data == 'predoplata_question':
        pic1 = open(r"C:\Users\nicki\Desktop\LuciviyBOT\src\question\pered.jpg", "rb")
        pic2 = open(r"C:\Users\nicki\Desktop\LuciviyBOT\src\question\pered1.jpg", "rb")
        media = [                               
                InputMediaPhoto(pic1),
                InputMediaPhoto(pic2),
                ]
        await bot.send_media_group(chat_id, media)
        await bot.send_message(chat_id, 'Важная информация о том, как у меня происходит предоплата',reply_markup=keyboard_end_question())


    #Свободные эскизы
    elif callback.data == 'free_sketch':
        photo = open(await FreeSketchRepository.get_photo_path_sketch(chat_id), 'rb')
        description = await FreeSketchRepository.get_photo_description_sketch(chat_id)
        if await FreeSketchRepository.get_id_free_sketch(chat_id) == 19:
            await bot.send_photo(chat_id, photo, description)
        else:
            await bot.send_photo(chat_id, photo, description, reply_markup=keybord_for_sketch())
        if await FreeSketchRepository.update_id_free_sketch(chat_id):
            user_name = await UserRepository.get_username(chat_id)
            await bot.send_message(chat_id, f'Спасибо, {user_name}, тобой были просмотренны все мои свободные эскизы.\nДальше они будут повторяться.', reply_markup=keybord_for_sketch())

    #Главное меню
    elif callback.data == 'menu':
        user_name = await UserRepository.get_username(chat_id)
        await bot.send_message(chat_id, f'🌚Главное меню🌚', reply_markup=keybord_menu())
        


    #Расчет стоимости татту
    elif callback.data == 'calc_tattoo':
        await bot.send_message(chat_id, "              <b>Дисклеймер</b>\n\nСтоимость тату зависит от нескольких факторов: размера, места нанесения и сложности рисунка (ведь на 10-ти сантиметрах можно сделать как  простой цветочек, так и портрет, естественно, сумма здесь будет разная ✨).\nСейчас мы рассчитаем примерную цену, исходя из первых двух факторов, но для точной стоимости необходимо будет скинуть Виктории пример картинки/эскиза или подробное описание идеи.", parse_mode='HTML')
        await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, давай начнем с участка кожи. Ты хочешь себе сделать:', reply_markup=keybord_skin())
    

    #Участок кожи
    elif callback.data == 'clear':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Пустой участок кожи')
        await bot.edit_message_text( f'На какой части тела ты хочешь сделать тату?',chat_id, callback.message.id, reply_markup=keybord_body())
    elif callback.data == 'scar':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Перекрытие шрамов')
        await bot.edit_message_text( f'На какой части тела ты хочешь сделать тату?',chat_id, callback.message.id, reply_markup=keybord_body())
    elif callback.data == 'old_tattoo':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Перекрытие старой тату')
        await bot.edit_message_text( f'На какой части тела ты хочешь сделать тату?',chat_id, callback.message.id, reply_markup=keybord_body())
    elif callback.data == 'correction_tattoo':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Коррекция старой тату')
        await bot.edit_message_text(f'На какой части тела ты хочешь сделать тату?',chat_id, callback.message.id, reply_markup=keybord_body())
        

    #Части тела
    elif callback.data =='hand':
        await bot.edit_message_text('А поточнее?',chat_id, callback.message.id, reply_markup=keybord_hand())
    elif callback.data =='leg':
        await bot.edit_message_text('А поточнее?',chat_id, callback.message.id, reply_markup=keybord_leg())
    elif callback.data =='torso':
        await bot.edit_message_text('А поточнее?',chat_id, callback.message.id, reply_markup=keybord_torso())
    elif callback.data =='back':
        await bot.edit_message_text('А поточнее?',chat_id, callback.message.id, reply_markup=keybord_back())
    elif callback.data =='head':
        await bot.edit_message_text('А поточнее?',chat_id, callback.message.id, reply_markup=keybord_head())
    elif callback.data =='neck':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Шея')
        await bot.edit_message_text('А поточнее?',chat_id, callback.message.id, reply_markup=keybord_neck())
    
    #Рука
    elif callback.data == 'shoulder':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Плечи')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'biceps':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Бицепс')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'triceps':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Трицепс')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'forearm':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Предплечье')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'elbow':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Локоть')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'bend':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Сгиб')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'brush':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Кисть')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'fingers':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Пальцы')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())

    #Нога
    elif callback.data == 'thigh':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Бедро')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'knee':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Колено')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'shin':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Голень')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'calf':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Икра')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'foot':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Стопа')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())


    #Торс
    elif callback.data == 'сhest':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Грудь')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'ribs':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Ребра')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'belly':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Живот')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'collarbones':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Ключицы')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())


    #Спина
    elif callback.data == 'shoulder_blades':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Лопатки')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'spine':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Позвоночник')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'small_back':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Пояница')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())


    #Шея
    elif callback.data == 'behind':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Сзади')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'side':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Сбоку')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'front':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Спереди')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    

    #Голова
    elif callback.data == 'face':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Лицо')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'ear':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'За ухом')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'temple':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Висок')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())
    elif callback.data == 'back_head':
        await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Затылок')
        await bot.edit_message_text('Укажи примерный размер желаемой тату.',chat_id, callback.message.id, reply_markup=keybord_size())

    #Большие проекты
    elif callback.data == 'sleeve':
        await bot.edit_message_text(f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Полноценный рукав. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy',chat_id, callback.message.id, reply_markup=keybord_for_calculate_end())
    elif callback.data == 'whole_leg':
        await bot.edit_message_text(f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Шея целеком. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy',chat_id, callback.message.id, reply_markup=keybord_for_calculate_end())
    elif callback.data == 'whole_torso':
        await bot.edit_message_text(f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Целый торс. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy',chat_id, callback.message.id, reply_markup=keybord_for_calculate_end())
    elif callback.data == 'whole_back':
        await bot.edit_message_text(f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Целая спина. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy',chat_id, callback.message.id, reply_markup=keybord_for_calculate_end())
    elif callback.data == 'entire_neck':
        await bot.edit_message_text(f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Шея целеком. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy',chat_id, callback.message.id, reply_markup=keybord_for_calculate_end())
    
    #Размер
    elif callback.data == 'do_10':
        price = await CalculСostRepository.get_cost_user_tattoo(chat_id, True)
        parametrs = await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)
        await bot.edit_message_text(f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {parametrs}. Стоимость твоей татуировки варьируется от {5000+price} до {9000+price}. Чтобы узнать точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy',chat_id, callback.message.id, reply_markup=keybord_for_calculate_end())
    elif callback.data == '10_15':
        parametrs = await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)
        price = await CalculСostRepository.get_cost_user_tattoo(chat_id, True)
        await bot.edit_message_text(f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {parametrs}. Стоимость твоей татуировки варьируется от {9000+price} до {14000+price}. Чтобы узнать точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy',chat_id, callback.message.id, reply_markup=keybord_for_calculate_end())
    elif callback.data == '15_30':
        parametrs = await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)
        price = await CalculСostRepository.get_cost_user_tattoo(chat_id, True)
        await bot.edit_message_text(f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {parametrs}. Стоимость твоей татуировки варьируется от {15000+price} до {22000+price}. Чтобы узнать точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy',chat_id, callback.message.id, reply_markup=keybord_for_calculate_end())
    elif callback.data == 'ot_30':
        parametrs = await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)
        price = await CalculСostRepository.get_cost_user_tattoo(chat_id, True)
        await bot.edit_message_text(f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {parametrs}. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy',chat_id, callback.message.id, reply_markup=keybord_for_calculate_end())







    # #Части тела
    # elif callback.data =='hand':
    #     await bot.send_message(chat_id, 'А поточнее?', reply_markup=keybord_hand())
    # elif callback.data =='leg':
    #     await bot.send_message(chat_id, 'А поточнее?', reply_markup=keybord_leg())
    # elif callback.data =='torso':
    #     await bot.send_message(chat_id, 'А поточнее?', reply_markup=keybord_torso())
    # elif callback.data =='back':
    #     await bot.send_message(chat_id, 'А поточнее?', reply_markup=keybord_back())
    # elif callback.data =='head':
    #     await bot.send_message(chat_id, 'А поточнее?', reply_markup=keybord_head())
    # elif callback.data =='neck':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Шея')
    #     await bot.send_message(chat_id, 'А поточнее?', reply_markup=keybord_neck())
    
    # #Рука
    # elif callback.data == 'shoulder':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Плечи')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'biceps':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Бицепс')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'triceps':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Трицепс')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'forearm':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Предплечье')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'elbow':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Локоть')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'bend':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Сгиб')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'brush':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Кисть')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'fingers':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Пальцы')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())

    # #Нога
    # elif callback.data == 'thigh':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Бедро')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'knee':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Колено')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'shin':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Голень')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'calf':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Икра')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'foot':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Стопа')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())


    # #Торс
    # elif callback.data == 'сhest':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Грудь')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'ribs':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Ребра')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'belly':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Живот')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'collarbones':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Ключицы')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())


    # #Спина
    # elif callback.data == 'shoulder_blades':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Лопатки')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'spine':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Позвоночник')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'small_back':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Пояница')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())


    # #Шея
    # elif callback.data == 'behind':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Сзади')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'side':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Сбоку')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'front':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Спереди')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    

    # #Голова
    # elif callback.data == 'face':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Лицо')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'ear':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'За ухом')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'temple':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 0, 'Висок')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())
    # elif callback.data == 'back_head':
    #     await CalculСostRepository.update_cost_and_parametrs_user_tattoo(chat_id, 1000, 'Затылок')
    #     await bot.send_message(chat_id, 'Укажи примерный размер желаемой тату.', reply_markup=keybord_size())

    # #Большие проекты
    # # elif callback.data == 'sleeve':
    #     # await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Полноценный рукав. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy', reply_markup=keybord_for_calculate_end())
    # elif callback.data == 'sleeve':
    #     await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Полноценный рукав. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy', reply_markup=keybord_for_calculate_end())
    # elif callback.data == 'whole_leg':
    #     await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Шея целеком. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy', reply_markup=keybord_for_calculate_end())
    # elif callback.data == 'whole_torso':
    #     await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Целый торс. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy', reply_markup=keybord_for_calculate_end())
    # elif callback.data == 'whole_back':
    #     await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Целая спина. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy', reply_markup=keybord_for_calculate_end())
    # elif callback.data == 'entire_neck':
    #     await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)}, Шея целеком. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy', reply_markup=keybord_for_calculate_end())
    
    # #Размер
    # elif callback.data == 'do_10':
    #     price = await CalculСostRepository.get_cost_user_tattoo(chat_id, True)
    #     parametrs = await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)
    #     await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {parametrs}. Стоимость твоей татуировки варьируется от {5000+price} до {9000+price}. Чтобы узнать точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy', reply_markup=keybord_for_calculate_end())
    # elif callback.data == '10_15':
    #     parametrs = await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)
    #     price = await CalculСostRepository.get_cost_user_tattoo(chat_id, True)
    #     await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {parametrs}. Стоимость твоей татуировки варьируется от {9000+price} до {14000+price}. Чтобы узнать точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy', reply_markup=keybord_for_calculate_end())
    # elif callback.data == '15_30':
    #     parametrs = await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)
    #     price = await CalculСostRepository.get_cost_user_tattoo(chat_id, True)
    #     await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {parametrs}. Стоимость твоей татуировки варьируется от {15000+price} до {22000+price}. Чтобы узнать точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy', reply_markup=keybord_for_calculate_end())
    # elif callback.data == 'ot_30':
    #     parametrs = await CalculСostRepository.get_prametrs_user_tattoo(chat_id, True)
    #     price = await CalculСostRepository.get_cost_user_tattoo(chat_id, True)
    #     await bot.send_message(chat_id, f'{await UserRepository.get_username(chat_id)}, тобой были выбраны параметры: {parametrs}. Все масштабные тату от 30 см я разбиваю на несколько сеансов. Цена 1-го сеанса - 12000. Чтобы узнать количество сеансов и точную стоимость, обсудить все детали и записаться на сеанс необходимо:\n\n1. Переслать мне это сообщение\n\n2. Прикрепить пример желаемого эскиза, либо подробно описать идею, чтобы я смогла создать индивидуальный эскиз\n\nНапиши мне: @luciviy', reply_markup=keybord_for_calculate_end())
        


#Запуск бота
async def main():
    await async_create_tables()
    await insert_data_in_free_scetch()
    await bot.polling(none_stop=True)

asyncio.run(main())