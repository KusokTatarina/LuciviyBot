from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import  sessionmaker
from sqlalchemy import create_engine


from database.models import Base

async_engine = create_async_engine("sqlite+aiosqlite:///async_main.db")
engine = create_engine("sqlite:///main.db")


async_session = async_sessionmaker(async_engine)
session = sessionmaker(engine)



async def async_create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def create_tables():
    Base.metadata.create_all(engine)

# def insert_data():
#     with session() as sess:
