from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.menu_ru import davom_buyurtma_ru
# from keyboards.default.menu_ru import tavarlar_ru

from loader import dp

tavar_malumotlari_800_ru = {1: "1. Английская Серия\nВ упаковке:\n\n- 400г Колбасок Куриных с Сыром\n"
                               "- 400г Колбасок Говяжьих\n\n85,000 сум/шт",
                            2: "2. Итальянская Коллекция\nВ упаковке:\n\n- 400г Колбасок Куриных с Зеленью\n"
                               "- 400г Колбасок Говяжьих с Зеленью\n\n85,000 сум/шт",
                            3: "3. Мексиканский Дуэт\nВ упаковке:\n\n- 400г Колбасок Куриных Острых\n"
                               "- 400г Колбасок Говяжьих Острых\n\n85,000 сум/шт",
                            4: "4. Французская Симфония\nВ упаковке:\n\n- 400г Колбасок 'Говяжьи с Сыром'\n"
                               "- 400г Колбасок 'из Баранины'\n\n90,000 сум/шт"
                            }


@dp.message_handler(text="Сеты - 800г")
async def calltavar_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"nomer_8_ru": 1}
    )

    mahsulotlar_inline_ru = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Подробнее", callback_data="dobavit_2_ru")
            ],
            [
                InlineKeyboardButton(
                    text="⬅",
                    callback_data="minus_2_ru"
                ),
                InlineKeyboardButton(
                    text="1/4",
                    callback_data="electronics_2_ru"
                ),
                InlineKeyboardButton(
                    text="➡",
                    callback_data="plus_2_ru"
                )
            ]
        ]
    )
    photo = open("./data/tavarlar/4_800/1.jpg", "rb")
    await message.answer_photo(photo=photo,
                               caption=f"1. Английская Серия\nВ упаковке:\n\n- 400г Колбасок Куриных с Сыром\n"
                                       "- 400г Колбасок Говяжьих\n\n85,000 сум/шт",
                               reply_markup=mahsulotlar_inline_ru)
    await message.delete()


@dp.callback_query_handler(lambda call: call.data == "minus_2_ru" or call.data == "plus_2_ru")
async def calltavar_ru(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_8_ru = data.get("nomer_8_ru")

    if nomer_8_ru is None:
        await call.message.delete()
    else:
        if call.data == "plus_2_ru":
            nomer_8_ru = nomer_8_ru + 1
        else:
            nomer_8_ru = nomer_8_ru - 1
        if nomer_8_ru == 5:
            nomer_8_ru = 1
        if nomer_8_ru == 0:
            nomer_8_ru = 4
        mahsulotlar_inline_ru = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Подробнее"
                                              "", callback_data="dobavit_2_ru")
                ],
                [
                    InlineKeyboardButton(
                        text="⬅",
                        callback_data="minus_2_ru"
                    ),
                    InlineKeyboardButton(
                        text=f"{nomer_8_ru}/4",
                        callback_data="electronics_2_ru"
                    ),
                    InlineKeyboardButton(
                        text="➡",
                        callback_data="plus_2_ru"
                    )
                ]
            ]
        )
        await state.update_data(
            {"nomer_8_ru": nomer_8_ru}
        )

        photo = open(f"./data/tavarlar/4_800/{nomer_8_ru}.jpg", "rb")
        await call.message.answer_photo(photo=photo, caption=f"{tavar_malumotlari_800_ru[nomer_8_ru]}",
                                        reply_markup=mahsulotlar_inline_ru)
        await call.message.delete()


# savatga qo'shish 1 qism


@dp.callback_query_handler(text="dobavit_2_ru")
async def dsfsefsf(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_8_ru = data.get("nomer_8_ru")

    if nomer_8_ru is None:
        await call.message.delete()
    else:
        buy_soni_8_ru = 1
        buyurtma_inline_ru = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="-",
                        callback_data="minus_buy_2_ru"
                    ),
                    InlineKeyboardButton(
                        text=f"{buy_soni_8_ru}",
                        callback_data="electronics_2_ru"
                    ),
                    InlineKeyboardButton(
                        text="+",
                        callback_data="plus_buy_2_ru"
                    )
                ]
            ]
        )
        await state.update_data(
            {"buy_soni_8_ru": buy_soni_8_ru}
        )
        await state.update_data(
            {"gr_ru": 800}
        )
        photo1 = open(f"./data/tavarlar/4_800/{nomer_8_ru}.jpg", "rb")
        photo2 = open(f"./data/tavarlar/4_800/{nomer_8_ru}_2.jpg", "rb")
        photo3 = open(f"./data/tavarlar/4_800/{nomer_8_ru}_3.jpg", "rb")
        await call.message.answer_photo(photo=photo1)
        await call.message.answer_photo(photo=photo2, reply_markup=davom_buyurtma_ru)
        await call.message.answer_photo(photo=photo3, caption=f"{tavar_malumotlari_800_ru[nomer_8_ru]}\n\n"
                                                              f"<b>Выберите количество:</b>",
                                        reply_markup=buyurtma_inline_ru)
        await call.message.delete()


@dp.callback_query_handler(lambda call: call.data == "minus_buy_2_ru" or call.data == "plus_buy_2_ru")
async def dsfsefsf_ru(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_8_ru = data.get("nomer_8_ru")
    buy_soni_8_ru = data.get("buy_soni_8_ru")

    if nomer_8_ru is None or buy_soni_8_ru is None:
        await call.message.delete()
    else:
        buy_soni_8_ru = int(buy_soni_8_ru)

        if call.data == "plus_buy_2_ru":
            buy_soni_8_ru = buy_soni_8_ru + 1
        else:
            buy_soni_8_ru = buy_soni_8_ru - 1

        if buy_soni_8_ru < 0:
            buy_soni_8_ru = 0
        buyurtma_inline_ru = InlineKeyboardMarkup(
            inline_keyboard=[
                # [
                #     InlineKeyboardButton(text="Добавить в корзину", callback_data="buyurtma_berish_800_ru")
                # ],
                [
                    InlineKeyboardButton(
                        text="-",
                        callback_data="minus_buy_2_ru"
                    ),
                    InlineKeyboardButton(
                        text=f"{buy_soni_8_ru}",
                        callback_data="electronics_2_ru"
                    ),
                    InlineKeyboardButton(
                        text="+",
                        callback_data="plus_buy_2_ru"
                    )
                ]
            ]
        )
        await state.update_data(
            {"buy_soni_8_ru": buy_soni_8_ru}
        )
        await state.update_data(
            {"gr_ru": 800}
        )
        await call.message.edit_reply_markup(reply_markup=buyurtma_inline_ru)
