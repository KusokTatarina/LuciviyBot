from sqlalchemy import insert, select, update
from sqlalchemy.exc import IntegrityError
from database.database import async_session
from database.models import *
# FreeScketch, KindSkin, User


class UserRepository:
    @staticmethod
    async def get_username(user_id: int):
        async with async_session() as sess:
            query = select(User.name).filter_by(user_id=user_id)
            result = await sess.execute(query)
            return result.scalar_one_or_none()

    @staticmethod
    async def add_user_or_update(user_id: int, user_name: str):
        try:
            async with async_session() as sess:
                stmt = insert(User).values(user_id=user_id, name=user_name)
                await sess.execute(stmt)
                await sess.commit()
                return await UserRepository.get_username(user_id)
            
        except IntegrityError:
            async with async_session() as sess:
                stmt = update(User).values(name=user_name).filter_by(user_id=user_id)
                await sess.execute(stmt)
                await sess.commit()
                return await UserRepository.get_username(user_id)
            
    @staticmethod
    async def register_user(user_id: int):
        async with async_session() as sess:
            stmt = update(User).values(user_regist=True).filter_by(user_id=user_id)
            await sess.execute(stmt)
            await sess.commit()
            return True
            
    @staticmethod
    async def check_register_user(user_id: int):
        async with async_session() as sess:
            query = select(User.user_regist).filter_by(user_id=user_id)
            result = await sess.execute(query)
            return result.scalar_one_or_none()


class FreeSketchRepository:
    @staticmethod
    async def get_id_free_sketch(user_id: int) -> int:
            async with async_session() as sess:
                query = select(User.free_sketch).filter_by(user_id=user_id)
                id_scetch = await sess.execute(query)
                return id_scetch.scalar_one_or_none()
    
    @staticmethod
    async def update_id_free_sketch(user_id: int):
            async with async_session() as sess:
                id_sketch_by_user = await FreeSketchRepository.get_id_free_sketch(user_id)
                if id_sketch_by_user == 19:
                    id_sketch_by_user = 1
                    stmt = update(User).values(free_sketch=id_sketch_by_user).filter_by(user_id=user_id)
                    await sess.execute(stmt)
                    await sess.commit()
                    return True
                else:
                    id_sketch_by_user += 1
                    stmt = update(User).values(free_sketch=id_sketch_by_user).filter_by(user_id=user_id)
                    await sess.execute(stmt)
                    await sess.commit()
                    return False
    
    @staticmethod
    async def get_photo_path_sketch(user_id: int) -> str:
            async with async_session() as sess:
                photo_id = await FreeSketchRepository.get_id_free_sketch(user_id)
                query = select(FreeScketch.path).filter_by(id=photo_id)
                photo_path = await sess.execute(query)
                return photo_path.scalar_one_or_none()
            
    @staticmethod
    async def get_photo_description_sketch(user_id: int) -> str:
            async with async_session() as sess:
                photo_id = await FreeSketchRepository.get_id_free_sketch(user_id)
                query = select(FreeScketch.description).filter_by(id=photo_id)
                photo_description = await sess.execute(query)
                return photo_description.scalar_one_or_none()
            

class CalculСostRepository:
    @staticmethod
    async def get_cost_user_tattoo(user_id: int, the_end: bool = False) -> int:
            async with async_session() as sess:
                query = select(User.cost_tattoo).filter_by(user_id=user_id)
                cost_tattoo = await sess.execute(query)
                cost_tattoo = cost_tattoo.scalar_one_or_none()
                if the_end:
                    stmt = update(User).values(cost_tattoo=0)
                    await sess.execute(stmt)
                    await sess.commit()
                return cost_tattoo
            
    @staticmethod
    async def get_prametrs_user_tattoo(user_id: int, the_end: bool = False) -> str:
            async with async_session() as sess:
                query = select(User.parametrs_tattoo).filter_by(user_id=user_id)
                parametrs_tattoo = await sess.execute(query)
                parametrs_tattoo = parametrs_tattoo.scalar_one_or_none()
                if the_end:
                    stmt = update(User).values(parametrs_tattoo='')
                    await sess.execute(stmt)
                    await sess.commit()
                return parametrs_tattoo
                
    @staticmethod
    async def update_cost_and_parametrs_user_tattoo(user_id: int, price: int, parametrs: str):
         async with async_session() as sess:
                cost_user = await CalculСostRepository.get_cost_user_tattoo(user_id)
                cost_tattoo = cost_user + price
                parametrs_tattoo = await CalculСostRepository.get_prametrs_user_tattoo(user_id)
                if parametrs_tattoo == '':
                     new_parametrs_tattoo = parametrs
                else:
                    new_parametrs_tattoo = parametrs_tattoo + ',' + parametrs
                stmt = update(User).values(cost_tattoo=cost_tattoo, parametrs_tattoo=new_parametrs_tattoo).filter_by(user_id=user_id)
                await sess.execute(stmt)
                await sess.commit()
            
    # @staticmethod
    # async def update_cost_and_parametrs_user_tattoo(user_id: int, price: int):
    #      async with async_session() as sess:
    #             cost_user = await CalculСostRepository.get_cost_user_tattoo(user_id)
    #             cost_tattoo = cost_user + price
    #             stmt = update(User).values(cost_tattoo=cost_tattoo)
    #             await sess.execute(stmt)
    #             await sess.commit()


    # async def update_parametrs_user_tattoo(user_id: int, parametrs: str):
    #      async with async_session() as sess:
    #             parametrs_tattoo = await CalculСostRepository.get_prametrs_user_tattoo(user_id)
    #             new_parametrs_tattoo = parametrs_tattoo + ',' + parametrs
    #             stmt = update(User).values(parametrs_tattoo=new_parametrs_tattoo)
    #             await sess.execute(stmt)
    #             await sess.commit()

async def take_counts_users():
    async with async_session() as session:
        query = select(User.id).order_by(User.id.desc()).limit(1)
        result = await session.execute(query)
        return result.scalar_one_or_none()
        

async def insert_data_in_free_scetch():
    async with async_session() as session:

        sketch1 = FreeScketch(path=r'free_sketch/1.jpg', description='1/19\n\n🖤Овен🖤\nСделаю в размере 15-30 см.\nСтоимость варьируется от размера, от 6.000-10.000')
        sketch2 = FreeScketch(path=r'free_sketch/2.jpg', description='2/19\n\n🖤Скорпион🖤\nСделаю в размере 15-30 см.\nСтоимость варьируется от размера, от 6.000-10.000')
        sketch3 = FreeScketch(path=r'free_sketch/3.jpg', description='3/19\n\n🖤Весы🖤\nСделаю в размере 15-30 см.\nСтоимость варьируется от размера, от 6.000-10.000')
        sketch4 = FreeScketch(path=r'free_sketch/4.jpg', description='4/19\n\n🖤Лев🖤\nСделаю в размере 15-30 см.\nСтоимость варьируется от размера, от 6.000-10.000')
        sketch5 = FreeScketch(path=r'free_sketch/5.jpg', description='5/19\n\n🖤Рак🖤\nСделаю в размере 15-30 см.\nСтоимость варьируется от размера, от 6.000-10.000')
        sketch6 = FreeScketch(path=r'free_sketch/6.jpg', description='6/19\n\n🖤Близнецы🖤\nСделаю в размере 15-30 см.\nСтоимость варьируется от размера, от 6.000-10.000')
        sketch7 = FreeScketch(path=r'free_sketch/7.jpg', description='7/19\n\n🖤Телец🖤\nСделаю в размере 15-30 см.\nСтоимость варьируется от размера, от 6.000-10.000')
        sketch8 = FreeScketch(path=r'free_sketch/8.jpg', description='8/19\n\nСвободные цветочные эскизы. Размер 15-20 см. \nСтоимость каждой - 6.000')
        sketch9 = FreeScketch(path=r'free_sketch/9.jpg', description='9/19\n\n🖤Всевидящие🖤\nРазмер 15-20 см. Стоимость любого эскиза - 6.000.')
        sketch10 = FreeScketch(path=r'free_sketch/10.jpg', description='10/19\n\n🖤Всевидящие🖤\nРазмер 15-20 см. Стоимость любого  эскиза - 6.000.')
        sketch11 = FreeScketch(path=r'free_sketch/11.jpg', description='11/19\n\n🖤Слепота🖤\nРазмер 20-25 см. Стоимость - 7.000')
        sketch12 = FreeScketch(path=r'free_sketch/12.jpg', description='12/19\n\n🖤Крылатые🖤\nРазмер в ширину - 15-20 см \nСтоимость каждой тату по этим эскизам - 7.000')
        sketch13 = FreeScketch(path=r'free_sketch/13.jpg', description='13/19\n\n🖤Сет парных татуировок🖤\nМожно сделать  и одну. \nСтоимость любого эскиза - 5.000')
        sketch14 = FreeScketch(path=r'free_sketch/14.jpg', description='14/19\n\n🖤Суккуб и Мутационный цветок🖤\nРазмер каждого эскиза - около 20 см. \nСтоимость каждого эскиза - 7.000')
        sketch15 = FreeScketch(path=r'free_sketch/15.jpg', description='15/19\n\n🖤Замок смерти, Всевидящие ягоды, Морской обитатель🖤\nРазмеры: \nЗамок - 15-23 см\nЯгоды - до 15 см \nМорской обитатель - до 15 см \n\nЦена:\nЗамок - 7.000\nЯгоды и обитатель морей - по 5.000')
        sketch16 = FreeScketch(path=r'free_sketch/16.jpg', description='16/19\n\n🖤Сонный паралич, Намакуби🖤\nРазмер каждого эскиза - 15-23 см. \nСтоимость любого эскиза - 7.000')
        sketch17 = FreeScketch(path=r'free_sketch/17.jpg', description='17/19\n\n 🖤Фламинго🖤\nПроект на целую спину. Делается в 5 сеансов длительностью не более 3-х часов. Стоимость одного сеанса - 9.000.')
        sketch18 = FreeScketch(path=r'free_sketch/18.jpg', description='18/19\n\n🖤Scorpio🖤\nРазмер данного эскиза 15-20 см, стоимость - 6.000.\nПредполагаемые места для нанесения: предплечье, плечо, бицепс, икра, голень, бедро, торс.')
        sketch19 = FreeScketch(path=r'free_sketch/19.jpg', description='19/19 \n\nПрайс на эскизы:\n🖤Морская ведьма🖤 - проект на целую внешнюю часть руки. Стоимость всего проекта - 27.000.\nПроект делается за 3 сеанса, длительность каждого - не более 3-х часов. Возможна оплата по сеансам.')
        

        session.add_all([sketch1,sketch2,sketch3,sketch4,sketch5,sketch6,sketch7,sketch8,sketch9,sketch10,sketch11,sketch12,sketch13,sketch14,sketch15,sketch16,sketch17,sketch18,sketch19])
        await session.commit()

# async def insert_data_in_kind_skin():
#      async with async_session() as session:
#         skin1 = KindSkin(skin='Чистый участок кожи',prise=0)
#         skin2 = KindSkin(skin='Перекрытие шрамов',prise=0)
#         skin3 = KindSkin(skin='Перекрытие старой татуировки',prise=2000)
#         skin4 = KindSkin(skin='Коррекция старой татуировки',prise=0)
#         session.add_all([skin1,skin2,skin3,skin4])
#         await session.commit()

# async def insert_data_in_body_part():
#      async with async_session() as session:
#         body1 = BodyPart(body='Плечо',trabl=0)
#         body2 = BodyPart(body='Бицепс',trabl=0)
#         body3 = BodyPart(body='Трицепс',trabl=0)
#         body4 = BodyPart(body='Предплечье',trabl=0)
#         body5 = BodyPart(body='Локоть',trabl=1000)
#         body6 = BodyPart(body='Сгиб',trabl=1000)
#         body7 = BodyPart(body='Кисть',trabl=1000)
#         body8 = BodyPart(body='Пальцы',trabl=1000)
#         body9 = BodyPart(body='Бедро',trabl=0)
#         body10 = BodyPart(body='Колено',trabl=1000)
#         body11 = BodyPart(body='Голен',trabl=0)
#         body12 = BodyPart(body='Икра',trabl=0)
#         body13 = BodyPart(body='Стопа',trabl=1000)
#         body14 = BodyPart(body='Грудь',trabl=0)
#         body15 = BodyPart(body='Ребра',trabl=1000)
#         body16 = BodyPart(body='Живот',trabl=1000)
#         body17 = BodyPart(body='Ключицы',trabl=0)
#         body18 = BodyPart(body='Лопатки',trabl=0)
#         body19 = BodyPart(body='Позвоночник',trabl=0)
#         body20 = BodyPart(body='Поясница',trabl=1000)
#         body21 = BodyPart(body='Шея-Сзади',trabl=1000)
#         body22 = BodyPart(body='Шея-Сбоку',trabl=1000)
#         body23 = BodyPart(body='Шея-Спереди',trabl=1000)
#         body24 = BodyPart(body='Лицо',trabl=0)
#         body25 = BodyPart(body='За ухом',trabl=0)
#         body26 = BodyPart(body='Висок',trabl=0)
#         body27 = BodyPart(body='Затылок',trabl=1000)

#         session.add_all([body1,body2,body3,body4,body5,body6,body7,body8,body9,body10,body11,body12,body13,
#                         body14,body15,body16,body17,body18,body19,body20,body21,body22,body23,body24,body25,
#                         body26,body27])
#         await session.commit()

# async def insert_data_in_body_part():
#      async with async_session() as session:
#         prise1 = PriseSize(size='До 10 см',price_ot=5000,price_do=5000)
#         prise2 = PriseSize(size='От 10 до 15 см',price_ot=9000,price_do=12000)
#         prise3 = PriseSize(size='От 15 до 30 см',price_ot=15000,price_do=5000)
#         prise4 = PriseSize(size='30 и более см',price_ot=5000,price_do=5000)
#         session.add_all([prise1,prise2,prise3,prise4])
#         await session.commit()