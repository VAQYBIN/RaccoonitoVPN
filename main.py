import asyncio

from aiogram import Bot, Dispatcher
from config import load_config
from handlers import menu
from middlewares.logging import LoggingMiddleware


async def main():
    config = load_config()
    if not config.bot_token:
        raise ValueError("BOT_TOKEN is not set")

    bot = Bot(token=config.bot_token)
    dp = Dispatcher()

    dp.include_routers(menu.router)

    dp.message.middleware(LoggingMiddleware())

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot was stopped manually")
    except Exception as e:
        print(f"Bot was stopped with error: {e}")
