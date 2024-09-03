import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.menu import tavarlar, davom_buyurtma
# from keyboards.inline.main_inline import mahsulotlar_nol
from loader import dp, bot

tavar_malumotlari_330 = {1: "1. Mo'l kolbasalari - Bavariya\nQadoqda - 330g\n\n40,000 UZS/dana",
                         2: "2. Mo'l kolbasalari ko'katlar bilan - Gatlinburg\nQadoqda - 330g\n\n40,000 UZS/dana",
                         3: "3. Mo'l kolbasalari achchiqroq - Peperoni\nQadoqda - 330g\n\n40,000 UZS/dana",
                         4: "4. Pishloqli Tovuqli Kolbasa - Haniken\nQadoqda - 330g\n\n35,000 UZS/dana",
                         5: "5. Tovuq kolbasalari ko'katlar bilan - Bratwurst\nQadoqda - 330g\n\n35,000 UZS/dana",
                         6: "6. Tovuq kolbasalari achchiqroq - Bombay\nQadoqda - 330g\n\n35,000 UZS/dana"
                         }


@dp.message_handler(text="🛍Buyurtma berish")
async def main1(message: types.Message):
    await message.answer(f"Tavarlar", reply_markup=tavarlar)


@dp.message_handler(text="Monopak kolbasa 330 g")
async def calltavar(message: types.Message, state: FSMContext):
    await state.update_data(
        {"nomer_3": 1}
    )

    mahsulotlar_inline = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Batafsil", callback_data="dobavit")
            ],
            [
                InlineKeyboardButton(
                    text="⬅",
                    callback_data="minus"
                ),
                InlineKeyboardButton(
                    text="1/6",
                    callback_data="electronics"
                ),
                InlineKeyboardButton(
                    text="➡",
                    callback_data="plus"
                )
            ]
        ]
    )
    photo = open("./data/tavarlar/6_330/1.jpg", "rb")
    await message.answer_photo(photo=photo, caption=f"Mo'l kolbasalari - Bavariya\nQadoqda - 330g\n\n40,000 UZS/dana ",
                               reply_markup=mahsulotlar_inline)
    await message.delete()


@dp.callback_query_handler(lambda call: call.data == "minus" or call.data == "plus")
async def calltavar(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_3 = data.get("nomer_3")

    if nomer_3 is None:
        await call.message.delete()
    else:

        if call.data == "plus":
            nomer_3 = nomer_3 + 1
        else:
            nomer_3 = nomer_3 - 1
        if nomer_3 == 7:
            nomer_3 = 1
        if nomer_3 == 0:
            nomer_3 = 6
        mahsulotlar_inline = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Batafsil", callback_data="dobavit")
                ],
                [
                    InlineKeyboardButton(
                        text="⬅",
                        callback_data="minus"
                    ),
                    InlineKeyboardButton(
                        text=f"{nomer_3}/6",
                        callback_data="electronics"
                    ),
                    InlineKeyboardButton(
                        text="➡",
                        callback_data="plus"
                    )
                ]
            ]
        )
        await state.update_data(
            {"nomer_3": nomer_3}
        )

        photo = open(f"./data/tavarlar/6_330/{nomer_3}.jpg", "rb")
        await call.message.answer_photo(photo=photo, caption=f"{tavar_malumotlari_330[nomer_3]}",
                                        reply_markup=mahsulotlar_inline)
        await call.message.delete()


# savatga qo'shish 1 qism
# savatga qo'shish 1 qism
# savatga qo'shish 1 qism
# savatga qo'shish 1 qism
# savatga qo'shish 1 qism
# savatga qo'shish 1 qism


@dp.callback_query_handler(text="dobavit")
async def dsfsefsf(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_3 = data.get("nomer_3")

    if nomer_3 is None:
        await call.message.delete()
    else:

        buy_soni_3 = 1
        buyurtma_inline = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="-",
                        callback_data="minus_buy_3"
                    ),
                    InlineKeyboardButton(
                        text=f"{buy_soni_3}",
                        callback_data="electronics_3"
                    ),
                    InlineKeyboardButton(
                        text="+",
                        callback_data="plus_buy_3"
                    )
                ]
            ]
        )
        await state.update_data(
            {"buy_soni_3": buy_soni_3}
        )
        await state.update_data(
            {"gr": 330}
        )

        photo1 = open(f"./data/tavarlar/6_330/{nomer_3}.jpg", "rb")
        photo2 = open(f"./data/tavarlar/6_330/{nomer_3}_2.jpg", "rb")
        await call.message.answer_photo(photo=photo1, reply_markup=davom_buyurtma)
        await call.message.answer_photo(photo=photo2, caption=f"{tavar_malumotlari_330[nomer_3]}\n\n"
                                                              f"<b>Miqdorni tanlang:</b>",
                                        reply_markup=buyurtma_inline)

        await call.message.delete()


async def delete_message(message: types.Message, delay: int):
    await asyncio.sleep(delay)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@dp.callback_query_handler(lambda call: call.data == "minus_buy_3" or call.data == "plus_buy_3")
async def dsfsefsf(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_3 = data.get("nomer_3")
    buy_soni_3 = (data.get("buy_soni_3"))

    if nomer_3 is None or buy_soni_3 is None:
        await call.message.delete()
    else:

        buy_soni_3 = int(buy_soni_3)
        if call.data == "plus_buy_3":
            buy_soni_3 = buy_soni_3 + 1
        else:
            buy_soni_3 = buy_soni_3 - 1

        if buy_soni_3 < 0:
            buy_soni_3 = 0
        buyurtma_inline = InlineKeyboardMarkup(
            inline_keyboard=[
                # [
                #     InlineKeyboardButton(text="Davom ettish", callback_data="buyurtma_berish_330")
                # ],
                [
                    InlineKeyboardButton(
                        text="-",
                        callback_data="minus_buy_3"
                    ),
                    InlineKeyboardButton(
                        text=f"{buy_soni_3}",
                        callback_data="electronics_3"
                    ),
                    InlineKeyboardButton(
                        text="+",
                        callback_data="plus_buy_3"
                    )
                ]
            ]
        )
        await state.update_data(
            {"buy_soni_3": buy_soni_3}
        )
        await state.update_data(
            {"gr": 330}
        )

        await call.message.edit_reply_markup(reply_markup=buyurtma_inline)
