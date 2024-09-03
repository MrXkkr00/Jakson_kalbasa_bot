import buttons as buttons
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mahsulotlar_nol = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="-",
                callback_data="minus"
            ),
            InlineKeyboardButton(
                text=f"0",
                callback_data="electronics"
            ),
            InlineKeyboardButton(
                text="+",
                callback_data="plus"
            )
        ]
    ]
)

mahsulotlar_no = types.InlineKeyboardMarkup(inline_keyboard=[
    [
        types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
        types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
    ],
    [
        types.InlineKeyboardButton(text="buyurtma berish", callback_data="num_finish")
    ],
])

# tavarlar = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="To'plamlar - 800 g"),
#             KeyboardButton(text="Monopak kolbasa 330 g"),
#         ],
#         [
#             KeyboardButton(text="🏠Bosh menu"),
#         ],
#     ]
# )
