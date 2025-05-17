import os
import sys
from pathlib import Path
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

# Добавляем путь к проекту
sys.path.append(str(Path(__file__).parent))

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# Импортируем handlers
from handlers import start, celebrity

dp.include_router(start.router)
dp.include_router(celebrity.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())