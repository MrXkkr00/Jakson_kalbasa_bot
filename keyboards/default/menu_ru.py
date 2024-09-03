from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

bosh_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍Заказать"),
        ],
        [
            KeyboardButton(text="🎁Акции"),
            KeyboardButton(text="🛒Корзина"),
        ],
        [
            KeyboardButton(text="🏢 О нас"),
            KeyboardButton(text="🇺🇿 O'zbek"),
        ],

    ], resize_keyboard=True
)

# [
#     KeyboardButton(text="Сеты - 800г"),
#     KeyboardButton(text="Moнопак сосисок 330г"),
# ],


tavarlar_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сеты - 800г"),
            KeyboardButton(text="Moнопак сосисок 330г"),
        ],
        [
            KeyboardButton(text="🏠Главное меню"),
        ],
    ], resize_keyboard=True
)

buyutma_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Завершение заказа"),
        ],
        [
            KeyboardButton(text="📝Добавить заказ"),
        ],
        [
            KeyboardButton(text="🔄Очистить корзину"),
        ],
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)

davom_buyurtma_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить в Корзину")
        ],
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)

dastavka_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚕 Доставка"),
            KeyboardButton(text="🏃️ Самовывоз"),
        ],
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)

olib_ketish_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Госпитальный Рынок"),
            KeyboardButton(text="Рынок Катартал"),
        ],
        [
            KeyboardButton(text="Рынок Аския"),
            KeyboardButton(text="Фархадский Рынок"),
        ],
        [
            KeyboardButton(text="Буз Базар"),
            KeyboardButton(text="Рынок Чимган"),
        ],
        [
            KeyboardButton(text="Рынок Сергели (Дех)"),
            KeyboardButton(text="Рынок Кадышева"),
        ],
        [
            KeyboardButton(text="📍 Определить ближайший филиал"),

        ],
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)


vaqt_lanlash_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ближайшее'),
            KeyboardButton(text='На Время')
        ],
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)



tolov_turi_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💳Оплатить через Click'),
            KeyboardButton(text="💵Оплата наличными")
        ],
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)




bosh_menu_only_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)