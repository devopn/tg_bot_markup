from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import *
from aiogram import types
from db.base import get_session


async def get_user(id:int) -> User:
    async with await get_session() as session:
        user = await session.execute(select(User).where(User.id == id))
        user = user.scalars().first()
        return user
    
async def create_user(user: types.User) -> User:
    async with await get_session() as session:
        session.add(user)
        await session.commit()

