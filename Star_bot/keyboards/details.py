from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def details_keyboard(url: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🔍 Подробнее в Википедии",
                url=url
            )]
        ]
    )