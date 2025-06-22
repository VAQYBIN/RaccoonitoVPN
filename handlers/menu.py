from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

import keyboards.menu as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Добро пожаловать в Raccoonito Shop! Выберите желаемое действие:", reply_markup=kb.menu)
