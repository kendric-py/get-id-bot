from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


client_router = Router()


@client_router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer(
        f'<b>Ваш ID:</b> <code>{message.from_user.id}</code>\
        \n<b>Your ID:</b> <code>{message.from_user.id}</code>'
    )
