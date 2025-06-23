from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Пробная подписка", callback_data="trial")],

    [InlineKeyboardButton(text="Купить подписку", callback_data="buy"),
     InlineKeyboardButton(text="Инструкция", url="https://telegra.ph/h3Instrukciya-po-podklyucheniyu-VPN-cherez-botah3-06-17")],

    [InlineKeyboardButton(text="Рефералы", callback_data="referrals"),
     InlineKeyboardButton(text="О сервисе", url="https://telegra.ph/O-servise-06-18")],

    [InlineKeyboardButton(text="Личный кабинет", callback_data="account")],
    [InlineKeyboardButton(text="Админка", callback_data="admin")],
])
