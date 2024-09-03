from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_invoice = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Invoice tekshirish"),
        ],

    ], resize_keyboard=True
)


admin_only = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh sahifa Admin"),
        ],

    ], resize_keyboard=True
)
