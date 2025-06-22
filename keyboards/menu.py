from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Пробная подписка", callback_data="trial")],

    [InlineKeyboardButton(text="Купить подписку", callback_data="buy"),
     InlineKeyboardButton(text="Инструкция", callback_data="instruction")],

    [InlineKeyboardButton(text="Рефералы", callback_data="referrals"),
     InlineKeyboardButton(text="О сервисе", callback_data="about")],

    [InlineKeyboardButton(text="Личный кабинет", callback_data="account")],
    [InlineKeyboardButton(text="Админка", callback_data="admin")],
])
