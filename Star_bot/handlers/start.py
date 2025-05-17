from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F  # Добавляем этот импорт
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="ℹ️ Помощь"))
    await message.answer(
        "🎬 <b>Бот для поиска дат рождения знаменитостей</b>\n\n"
        "Просто напишите имя актёра, певца или режиссёра!\n"
        "Например: <i>Леонардо Ди Каприо</i>",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )

@router.message(F.text == "ℹ️ Помощь")
async def help_command(message: types.Message):
    await message.answer(
        "🔍 <b>Как пользоваться ботом:</b>\n\n"
        "1. Просто введите имя знаменитости\n"
        "2. Бот найдёт дату рождения\n\n"
        "<b>Примеры:</b>\n"
        "• Том Круз\n"
        "• Брэд Питт\n"
        "• Анджелина Джоли\n"
        "• Джонни Депп\n\n"
        "Работает для актёров, певцов, режиссёров и других знаменитостей!"
    )