import asyncio, os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_TELEGRAM_ID', '0'))
DOMAIN = os.getenv('DOMAIN', 'localhost')

async def on_startup(bot: Bot):
    if ADMIN_ID:
        await bot.send_message(ADMIN_ID, "Bot started")

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def start(m: Message):
        kb = InlineKeyboardMarkup(inline_keyboard=[[
            [InlineKeyboardButton(text="Open RentMini", web_app=WebAppInfo(url=f"https://{DOMAIN}"))]
        ]])
        await m.answer("Welcome to RentMini v2", reply_markup=kb)

    await on_startup(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
