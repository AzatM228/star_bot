from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from services.wikidata import get_celebrity_info
from keyboards.details import details_keyboard

router = Router()

@router.message(F.text & ~F.text.in_(["ℹ️ Помощь"]))  # Игнорируем кнопку помощи
async def handle_celebrity_request(message: types.Message):
    name = message.text.strip()
    if len(name) < 2:
        await message.answer("❌ Имя слишком короткое. Введите полное имя.")
        return

    data = await get_celebrity_info(name)

    if not data:
        await message.answer(
            "🚫 Не удалось найти информацию.\n"
            "Попробуйте:\n"
            "- Уточнить имя (например, 'Том Круз' вместо 'Том')\n"
            "- Проверить правильность написания"
        )
        return

    response = (
        f"🌟 <b>{data['name']}</b>\n"
        f"📅 <b>Дата рождения:</b> {data['birthday']}\n"
    )

    await message.answer(
        response,
        reply_markup=details_keyboard(data["url"])
    )