# bot.py
import asyncio
import os
from aiogram import Bot, Dispatcher
from handlers.basic import router


# Ініціалізація бота та бази даних
bot = Bot(token="7989896147:AAEz0LwlJPQRU4mstqNuBklhD0RNAa5wu1")
dp = Dispatcher()


# Підключення роутера
dp.include_router(router)

async def main():
    print("🚀 Бот запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




