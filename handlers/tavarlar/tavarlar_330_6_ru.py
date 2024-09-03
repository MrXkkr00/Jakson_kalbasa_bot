from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.menu_ru import tavarlar_ru, davom_buyurtma_ru
from loader import dp

tavar_malumotlari_330_ru = {1: "1.Колбаски Говяжьи - Баварские\nВ упаковке - 330г\n\n40,000 сум/шт",
                            2: "2. Колбаски Говяжьи с Зеленью - Гатлинбург\nВ упаковке - 330г\n\n40,000 сум/шт",
                            3: "3. Колбаски Говяжьи Пикантные - Пеперони\nВ упаковке - 330г\n\n40,000 сум/шт",
                            4: "4. Колбаски Куриные с Сыром - Ханикен\nВ упаковке - 330г\n\n35,000 сум/шт",
                            5: "5. Колбаски Куриные с Зеленью - Братвурст\nВ упаковке - 330г\n\n35,000 сум/шт",
                            6: "6. Колбаски Куриные Пикантные - Бомбей\nВ упаковке - 330г\n\n35,000 сум/шт"
                            }


@dp.message_handler(text="🛍Заказать")
async def main1_ru(message: types.Message):
    await message.delete()

    await message.answer(f"Товары", reply_markup=tavarlar_ru)


@dp.message_handler(text="Moнопак сосисок 330г")
async def calltavar_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"nomer_3_ru": 1}
    )

    mahsulotlar_inline_ru = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Подробнее", callback_data="dobavit_ru")
            ],
            [
                InlineKeyboardButton(
                    text="⬅",
                    callback_data="minus_ru"
                ),
                InlineKeyboardButton(
                    text="1/6",
                    callback_data="electronics_ru"
                ),
                InlineKeyboardButton(
                    text="➡",
                    callback_data="plus_ru"
                )
            ]
        ]
    )
    photo_ru = open("./data/tavarlar/6_330/1.jpg", "rb")
    await message.answer_photo(photo=photo_ru, caption=f"1.Колбаски Говяжьи - Баварские\n"
                                                       f"В упаковке - 330г\n\n40,000 сум/шт",
                               reply_markup=mahsulotlar_inline_ru)
    await message.delete()


@dp.callback_query_handler(lambda call: call.data == "minus_ru" or call.data == "plus_ru")
async def calltavar_ru(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_3_ru = data.get("nomer_3_ru")

    if nomer_3_ru is None:
        await call.message.delete()
    else:

        if call.data == "plus_ru":
            nomer_3_ru = nomer_3_ru + 1
        else:
            nomer_3_ru = nomer_3_ru - 1
        if nomer_3_ru == 7:
            nomer_3_ru = 1
        if nomer_3_ru == 0:
            nomer_3_ru = 6
        mahsulotlar_inline_ru = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Подробнее", callback_data="dobavit_ru")
                ],
                [
                    InlineKeyboardButton(
                        text="⬅",
                        callback_data="minus_ru"
                    ),
                    InlineKeyboardButton(
                        text=f"{nomer_3_ru}/6",
                        callback_data="electronics_ru"
                    ),
                    InlineKeyboardButton(
                        text="➡",
                        callback_data="plus_ru"
                    )
                ]
            ]
        )
        await state.update_data(
            {"nomer_3_ru": nomer_3_ru}
        )

        photo = open(f"./data/tavarlar/6_330/{nomer_3_ru}.jpg", "rb")
        await call.message.answer_photo(photo=photo, caption=f"{tavar_malumotlari_330_ru[nomer_3_ru]}",
                                        reply_markup=mahsulotlar_inline_ru)
        await call.message.delete()


# savatga qo'shish 1_ru qism


@dp.callback_query_handler(text="dobavit_ru")
async def dsfsefsf_ru(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_3_ru = data.get("nomer_3_ru")

    if nomer_3_ru is None:
        await call.message.delete()
    else:

        buy_soni_3_ru = 1
        buyurtma_inline_ru = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="-",
                        callback_data="minus_buy_3_ru"
                    ),
                    InlineKeyboardButton(
                        text=f"{buy_soni_3_ru}",
                        callback_data="electronics_3_ru"
                    ),
                    InlineKeyboardButton(
                        text="+",
                        callback_data="plus_buy_3_ru"
                    )
                ]
            ]
        )
        await state.update_data(
            {"buy_soni_3_ru": buy_soni_3_ru}
        )
        await state.update_data(
            {"gr_ru": 330}
        )
        photo1 = open(f"./data/tavarlar/6_330/{nomer_3_ru}.jpg", "rb")
        photo2 = open(f"./data/tavarlar/6_330/{nomer_3_ru}_2.jpg", "rb")
        await call.message.answer_photo(photo=photo1, reply_markup=davom_buyurtma_ru)
        await call.message.answer_photo(photo=photo2, caption=f"{tavar_malumotlari_330_ru[nomer_3_ru]}\n\n"
                                                              f"<b>Выберите количество:</b>",
                                        reply_markup=buyurtma_inline_ru)

        await call.message.delete()


@dp.callback_query_handler(lambda call: call.data == "minus_buy_3_ru" or call.data == "plus_buy_3_ru")
async def dsfsefsf_ru(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_3_ru = data.get("nomer_3_ru")
    buy_soni_3_ru = (data.get("buy_soni_3_ru"))

    if nomer_3_ru is None or buy_soni_3_ru is None:
        await call.message.delete()
    else:

        buy_soni_3_ru = int(buy_soni_3_ru)

        if call.data == "plus_buy_3_ru":
            buy_soni_3_ru = buy_soni_3_ru + 1
        else:
            buy_soni_3_ru = buy_soni_3_ru - 1

        if buy_soni_3_ru < 0:
            buy_soni_3_ru = 0
        buyurtma_inline_ru = InlineKeyboardMarkup(
            inline_keyboard=[
                # [
                #     InlineKeyboardButton(text="Добавить в корзину", callback_data="buyurtma_berish_800_ru")
                # ],
                [
                    InlineKeyboardButton(
                        text="-",
                        callback_data="minus_buy_3_ru"
                    ),
                    InlineKeyboardButton(
                        text=f"{buy_soni_3_ru}",
                        callback_data="electronics_3_ru"
                    ),
                    InlineKeyboardButton(
                        text="+",
                        callback_data="plus_buy_3_ru"
                    )
                ]
            ]
        )
        await state.update_data(
            {"buy_soni_3_ru": buy_soni_3_ru}
        )
        await state.update_data(
            {"gr_ru": 330}
        )

        await call.message.edit_reply_markup(reply_markup=buyurtma_inline_ru)
