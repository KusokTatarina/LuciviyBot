
from telebot import types

#Кнопкки главного меню
def keybord_menu():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('О себе', callback_data='myself'))
    bt5 = (types.InlineKeyboardButton('Часто задаваемые вопросы', callback_data='question'))
    bt2 = (types.InlineKeyboardButton('Мои свободные эскизы', callback_data='free_sketch'))
    bt3 = (types.InlineKeyboardButton('Примеры моих работ', callback_data='my_work'))
    bt4 = (types.InlineKeyboardButton('Рассчитать стоимость татуировки', callback_data='calc_tattoo'))
    markup.row(bt4)
    markup.row(bt2)
    markup.row(bt1)
    markup.row(bt3)
    markup.row(bt5)
    return markup

#Кнопки Обо мне
def keybord_myself():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Мой ВК', url='https://vk.com/viktoria_dahmer'))
    bt2 = (types.InlineKeyboardButton('Мой Инстаграмм', url='https://www.instagram.com/_lucivictor?igsh=MTY5OXF3bXRoenp4aA=='))
    bt3 = (types.InlineKeyboardButton('Моя группа в ВК', url='https://vk.com/luciviytattooo'))
    bt4 = (types.InlineKeyboardButton('Мой Телеграмм Канал', url='https://t.me/luciviytattoo'))
    bt5 = (types.InlineKeyboardButton('Вернуться в Меню', callback_data='menu'))
    markup.row(bt1,bt2)
    markup.row(bt3,bt4)
    markup.row(bt5)
    return markup


#Кнопки для Вопросов
def keybord_question():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('🪦 Как проходит сеанс ', callback_data='seans_question'))
    bt2 = (types.InlineKeyboardButton('🪦 Противопоказания к тату', callback_data='protivopokaz_question'))
    bt3 = (types.InlineKeyboardButton('🪦 Уход за татуировкой', callback_data='uhod_question'))
    bt4 = (types.InlineKeyboardButton('🪦 Информация о предоплате', callback_data='predoplata_question'))
    bt5 = (types.InlineKeyboardButton('Вернуться в Меню', callback_data='menu'))
    markup.row(bt1)
    markup.row(bt2)
    markup.row(bt3)
    markup.row(bt4)
    markup.row(bt5)
    return markup


#Кнопки в конце вопросов
def keyboard_end_question():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Ещё вопросы', callback_data='question'))
    bt2 = (types.InlineKeyboardButton('Вернуться в меню', callback_data='menu'))
    markup.row(bt1, bt2)
    return markup


#Кнопки Да и Нет для регистрации пользователя
def keyboard_yes_or_no():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Да', callback_data='yes'))
    bt2 = (types.InlineKeyboardButton('Нет', callback_data='no'))
    markup.row(bt1, bt2)
    return markup


#Кнопки свободных Эскизов
def keybord_for_sketch():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Показать ещё', callback_data='free_sketch'))
    bt2 = (types.InlineKeyboardButton('Вернуться в Меню', callback_data='menu'))
    markup.row(bt1)
    markup.row(bt2)
    return markup

#После получения стоимости
def keybord_for_calculate_end():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Попробовать еще', callback_data='calc_tattoo'))
    bt2 = (types.InlineKeyboardButton('Вернуться в Меню', callback_data='menu'))
    bt3 = (types.InlineKeyboardButton('Записаться на сеанс', url='https://t.me/luciviy'))
    markup.row(bt1, bt2)
    markup.row(bt3)
    return markup

#Кнопкки для состояния кожи
def keybord_skin():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Тату на пустом участке кожи', callback_data='clear'))
    markup.add(types.InlineKeyboardButton('Перекрытие шрамов', callback_data='scar'))
    markup.add(types.InlineKeyboardButton('Перекрытие старой тату', callback_data='old_tattoo'))
    markup.add(types.InlineKeyboardButton('Коррекцию старой тату', callback_data='correction_tattoo'))
    return markup

#Кнопкки для части тела
def keybord_body():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Рука', callback_data='hand'))
    bt2 = (types.InlineKeyboardButton('Нога', callback_data='leg'))
    bt3 = (types.InlineKeyboardButton('Торс', callback_data='torso'))
    bt4 = (types.InlineKeyboardButton('Спина', callback_data='back'))
    bt5 = (types.InlineKeyboardButton('Голова', callback_data='head'))
    bt6 = (types.InlineKeyboardButton('Шея', callback_data='neck'))

    markup.row(bt1,bt2)
    markup.row(bt3,bt4)
    markup.row(bt5,bt6)
    return markup

#Кнопкки для руки
def keybord_hand():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Плечо', callback_data='shoulder'))
    bt2 = (types.InlineKeyboardButton('Бицепс', callback_data='biceps'))
    bt3 = (types.InlineKeyboardButton('Трицепс', callback_data='triceps'))
    bt4 = (types.InlineKeyboardButton('Предплечье', callback_data='forearm'))
    bt5 = (types.InlineKeyboardButton('Локоть', callback_data='elbow'))
    bt6 = (types.InlineKeyboardButton('Сгиб', callback_data='bend'))
    bt7 = (types.InlineKeyboardButton('Кисть', callback_data='brush'))
    bt8 = (types.InlineKeyboardButton('Пальцы', callback_data='fingers'))
    bt9 = (types.InlineKeyboardButton('Полноценный Рукав', callback_data='sleeve'))
    # markup.row(bt1,bt2)
    # markup.row(bt3,bt4)
    # markup.row(bt5,bt6)
    # markup.row(bt7,bt8)
    # markup.row(bt9)
    markup.row(bt1,bt2,bt3)
    markup.row(bt4,bt5,bt6)
    markup.row(bt7,bt8)
    markup.row(bt9)

    return markup

#Кнопкки для ноги
def keybord_leg():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Бедро', callback_data='thigh'))
    bt2 = (types.InlineKeyboardButton('Колено', callback_data='knee'))
    bt3 = (types.InlineKeyboardButton('Голень', callback_data='shin'))
    bt4 = (types.InlineKeyboardButton('Икра', callback_data='calf'))
    bt5 = (types.InlineKeyboardButton('Стопа', callback_data='foot'))
    bt6 = (types.InlineKeyboardButton('Целая нога', callback_data='whole_leg'))
    markup.row(bt1,bt2,bt3)
    markup.row(bt4,bt5)
    markup.row(bt6)
    # markup.row(bt9)
    return markup

#Кнопкки для торса
def keybord_torso():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Грудь', callback_data='сhest'))
    bt2 = (types.InlineKeyboardButton('Ребра', callback_data='ribs'))
    bt3 = (types.InlineKeyboardButton('Живот', callback_data='belly'))
    bt4 = (types.InlineKeyboardButton('Ключицы', callback_data='collarbones'))
    bt5 = (types.InlineKeyboardButton('Целый торс', callback_data='whole_torso'))
    markup.row(bt1,bt2)
    markup.row(bt3,bt4)
    markup.row(bt5)
    return markup


#Кнопкки для спины
def keybord_back():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Лопатки', callback_data='shoulder_blades'))
    bt2 = (types.InlineKeyboardButton('Позвоночник', callback_data='spine'))
    bt3 = (types.InlineKeyboardButton('Поясница', callback_data='small_back'))
    bt4 = (types.InlineKeyboardButton('Целая спина', callback_data='whole_back'))
    markup.row(bt1,bt2,bt3)
    markup.row(bt4)
    # markup.row(bt5)
    return markup


#Кнопкки для шеи
def keybord_neck():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Сзади', callback_data='behind'))
    bt2 = (types.InlineKeyboardButton('Сбоку', callback_data='side'))
    bt3 = (types.InlineKeyboardButton('Спереди', callback_data='front'))
    bt4 = (types.InlineKeyboardButton('Шея целеком', callback_data='entire_neck'))
    markup.row(bt1,bt2,bt3)
    markup.row(bt4)
    # markup.row(bt5)
    return markup


#Кнопкки для головы
def keybord_head():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('Лицо', callback_data='face'))
    bt2 = (types.InlineKeyboardButton('За хуом', callback_data='ear'))
    bt3 = (types.InlineKeyboardButton('Висок', callback_data='temple'))
    bt4 = (types.InlineKeyboardButton('Затылок', callback_data='back_head'))
    markup.row(bt1,bt2)
    markup.row(bt3,bt4)
    # markup.row(bt5)
    return markup

#Кнопкки для размера
def keybord_size():
    markup = types.InlineKeyboardMarkup()
    bt1 = (types.InlineKeyboardButton('До 10 см', callback_data='do_10'))
    bt2 = (types.InlineKeyboardButton('От 10 до 15 см', callback_data='10_15'))
    bt3 = (types.InlineKeyboardButton('От 15 до 30 см', callback_data='15_30'))
    bt4 = (types.InlineKeyboardButton('30 и более см', callback_data='ot_30'))
    markup.row(bt1, bt2)
    markup.row(bt3, bt4)
    return markup