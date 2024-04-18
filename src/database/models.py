# from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'User'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str]
    free_sketch: Mapped[int] = mapped_column(default=1)
    user_regist: Mapped[bool] = mapped_column(default=False)
    cost_tattoo: Mapped[int] = mapped_column(default=0)
    parametrs_tattoo: Mapped[str] = mapped_column(default='')


class FreeScketch(Base):
    __tablename__ = 'FreeScketch'
    id: Mapped[int] = mapped_column(primary_key=True)
    path: Mapped[str]
    description: Mapped[Optional[str]]
    
# class KindSkin(Base):
#     __tablename__ = 'KindSkin'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     skin: Mapped[str]
#     prise: Mapped[int]
    

# class BodyPart(Base):
#     __tablename__ = 'PriceBody'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     body: Mapped[str]
#     do10: Mapped[int]
#     ot10: Mapped[int]

# class BodyPart(Base):
#     __tablename__ = 'BodyPart'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     body: Mapped[str]
#     trabl: Mapped[int]

# class PriseSize(Base):
#     __tablename__ = 'PriseSize'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     size: Mapped[str]
#     price_ot: Mapped[int]
#     price_do: Mapped[int]