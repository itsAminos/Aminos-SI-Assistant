from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # The 'await' yields control while sending the network request to Telegram
    await message.answer(f"Hello, {message.from_user.first_name}. I am operational.")

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Send me a message and I will process it asynchronously.")