from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [
                                               KeyboardButton(text="📱Kontakt",
                                                              request_contact=True)
                                           ]
                                       ])

contact_keyboard_ru = ReplyKeyboardMarkup(resize_keyboard=True,
                                          keyboard=[
                                              [
                                                  KeyboardButton(text="📱Контакт",
                                                                 request_contact=True)
                                              ]
                                          ])

til_tanlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbek"),
            KeyboardButton(text="🇷🇺Русский")
        ],

    ], resize_keyboard=True
)

locatsiya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍Joylashuvni yuborish",
                           request_location=True)
        ],
        [
            KeyboardButton(text="🏠Bosh menu")
        ]
    ], resize_keyboard=True
)


locatsiya_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍Отправить местоположение",
                           request_location=True)
        ],
        [
            KeyboardButton(text="🏠Главное меню")
        ]
    ], resize_keyboard=True
)
