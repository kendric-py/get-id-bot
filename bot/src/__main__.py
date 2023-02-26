from aiogram import Bot, Dispatcher

from telegram.middlewares.RegistrationMiddleware import RegistrationMiddleware
from telegram.middlewares.DatabaseMiddleware import DatabaseMiddleware
from telegram.routers.client.handlers import client_router

from database.manage import async_session

from config import BOT_TOKEN

import asyncio


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode='html')
    dp = Dispatcher()

    dp.update.outer_middleware(DatabaseMiddleware())
    dp.message.middleware(RegistrationMiddleware())

    dp.include_router(client_router)

    await dp.start_polling(bot, async_session=async_session)


asyncio.run(main())
