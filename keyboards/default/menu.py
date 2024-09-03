from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍Buyurtma berish "),
        ],
        [
            KeyboardButton(text="🎁Aksiya"),
            KeyboardButton(text="🛒Savat"),
        ],
        [
            KeyboardButton(text="🏢Biz haqimizda"),
            KeyboardButton(text="🇷🇺Русский"),
        ],

    ], resize_keyboard=True
)

# [
#     KeyboardButton(text="Сеты - 800г"),
#     KeyboardButton(text="Moнопак сосисок 330г"),
# ],


tavarlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="To'plamlar - 800 g"),
            KeyboardButton(text="Monopak kolbasa 330 g"),
        ],
        [
            KeyboardButton(text="🏠Bosh menu"),
        ],
    ], resize_keyboard=True
)

buyutma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅Buyurtmani amalga oshirish"),
        ],
        [
            KeyboardButton(text="📝Buyurtma qo'shish"),
        ],
        [
            KeyboardButton(text="🔄Savatni tozalash"),
        ],
        [
            KeyboardButton(text="🏠Bosh menu")
        ]
    ], resize_keyboard=True
)

davom_buyurtma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Savatga qo'shish")
        ],
        [
            KeyboardButton(text="🏠Bosh menu")
        ]
    ], resize_keyboard=True
)

dastavka = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚕 Yetkazib berish"),
            KeyboardButton(text="🏃️ Olib ketish"),
        ],
        [
            KeyboardButton(text="🏠Bosh menu")
        ]
    ], resize_keyboard=True
)

olib_ketish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kasalxona bozori"),
            KeyboardButton(text="Qatortol bozori"),
        ],
        [
            KeyboardButton(text="Askiya bozori"),
            KeyboardButton(text="Farxod bozori"),
        ],
        [
            KeyboardButton(text="Buz bozori"),
            KeyboardButton(text="Chimgan bozori"),
        ],
        [
            KeyboardButton(text="Sergili (Dehqon) bozori"),
            KeyboardButton(text="Qadsheva bozori"),
        ],
        [
            KeyboardButton(text="📍 Eng yaqin filialni topish"),
        ],
        [
            KeyboardButton(text="🏠Bosh menu")
        ]
    ], resize_keyboard=True
)

vaqt_lanlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Hozir'),
            KeyboardButton(text='Vaqtni tanlash')
        ],
        [
            KeyboardButton(text="🏠Bosh menu")
        ]
    ], resize_keyboard=True
)

tolov_turi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💳Click orqali toʻlash'),
            KeyboardButton(text="💵Naqd to'lash")
        ],
        [
            KeyboardButton(text="🏠Bosh menu")
        ]
    ], resize_keyboard=True
)

bosh_menu_only = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠Bosh menu")
        ]
    ], resize_keyboard=True
)
