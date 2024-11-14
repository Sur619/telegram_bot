from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_keyboard(questions):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for question in questions[:10]:  # Limit to 10 questions for the keyboard
        button_text = f"• {question.id}. {question.question[:50]}..."
        keyboard.inline_keyboard.append([InlineKeyboardButton(text=button_text, callback_data=f"show_{question.id}")])
    return keyboard
