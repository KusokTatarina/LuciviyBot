from telebot.types import InputMediaPhoto

def group_my_photo():
        pic1 = open(r"myself/1.jpg", "rb")
        pic2 = open(r"myself/2.jpg", "rb")
        pic3 = open(r"myself/3.jpg", "rb")
        pic4 = open(r"myself/4.jpg", "rb")
        pic5 = open(r"myself/5.jpg", "rb")
        pic6 = open(r"myself/6.jpg", "rb")
        pic7 = open(r"myself/7.jpg", "rb")

        
        media = [InputMediaPhoto(pic1, 
                                caption="О себе: \n\n💀Приветствую💀\n\n•Меня зовут Виктория, занимаюсь татуировкой с 2017-го года\n\n•Работаю в прекрасной  студии Inkk Noire в городе Пскове, иногда работаю в СПб, также в планах посетить другие города, вся информация о посещении других городов  и свободных днях на тату выкладывается в соц сети\n\n•Делаю только черные тату, они никогда не потеряют свою актуальность ✨\n\n•Использую только качественные и одноразовые расходные материалы, все вскрывается при тебе  на сеансе\n\n•Нарисую эскиз по твоей идее и размещу его на теле, исходя из твоей анатомии \n\n•Перекрываю шрамы и старые неудачные тату \n\n•Тебе не придется сидеть на сеансе целый день, так как сеансы длятся не дольше 3-х часов\n\n•Татуировки по моим свободным эскизам всегда по лояльной цене 🖤\nЗапись на сеанс/консультацию: @luciviy\n"), 
                                InputMediaPhoto(pic2),
                                InputMediaPhoto(pic3),
                                InputMediaPhoto(pic4),
                                InputMediaPhoto(pic5),
                                InputMediaPhoto(pic6),
                                InputMediaPhoto(pic7),
                                ]
        return media
