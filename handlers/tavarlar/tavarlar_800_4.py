from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.menu import davom_buyurtma
from loader import dp

tavar_malumotlari_800 = {1: "Inglizcha Seriya\n Qadoqda:\n\n- 400g Pishloqli Tovuqli Kolbasa\n"
                            "- 400g Mol Go'shtli Kolbasa\n\n85,000 UZS/dana",
                         2: "Italyancha Kolleksiya\nQadoqda:\n\n- 400g Ko'katli Tovuqli  Kolbasa\n"
                            "- 400g Ko'katli Mol Go'shtli Kolbasa\n\n85,000 UZS/dana",
                         3: "Meksikancha Duet\nQadoqda:\n\n- 400g Achchiq Tovuqli Kolbasa\n"
                            "- 400g Achchiq Mol Go'shtli Kolbasa\n\n85,000 UZS/dana",
                         4: "Fransuzcha Simfoniya\nQadoqda:\n\n- 400g Pishloqli Mol Go'shtli Kolbasa\n"
                            "- 400g Qo'zichoq Go'shtli Kolbasa\n\n90,000 UZS/dana"
                         }


@dp.message_handler(text="To'plamlar - 800 g")
async def calltavar(message: types.Message, state: FSMContext):
    await state.update_data(
        {"nomer_8": 1}
    )

    mahsulotlar_inline = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Batafsil", callback_data="dobavit_2")
            ],
            [
                InlineKeyboardButton(
                    text="⬅",
                    callback_data="minus_2"
                ),
                InlineKeyboardButton(
                    text="1/4",
                    callback_data="electronics_2"
                ),
                InlineKeyboardButton(
                    text="➡",
                    callback_data="plus_2"
                )
            ]
        ]
    )
    photo = open("./data/tavarlar/4_800/1.jpg", "rb")
    await message.answer_photo(photo=photo, caption=f"Mo'l kolbasalari - Bavariya\nQadoqda - 330g\n\n40,000 UZS/dana",
                               reply_markup=mahsulotlar_inline)
    await message.delete()


@dp.callback_query_handler(lambda call: call.data == "minus_2" or call.data == "plus_2")
async def calltavar(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_8 = data.get("nomer_8")

    if nomer_8 is None:
        await call.message.delete()
    else:

        if call.data == "plus_2":
            nomer_8 = nomer_8 + 1
        else:
            nomer_8 = nomer_8 - 1
        if nomer_8 == 5:
            nomer_8 = 1
        if nomer_8 == 0:
            nomer_8 = 4
        mahsulotlar_inline = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Batafsil", callback_data="dobavit_2")
                ],
                [
                    InlineKeyboardButton(
                        text="⬅",
                        callback_data="minus_2"
                    ),
                    InlineKeyboardButton(
                        text=f"{nomer_8}/4",
                        callback_data="electronics_2"
                    ),
                    InlineKeyboardButton(
                        text="➡",
                        callback_data="plus_2"
                    )
                ]
            ]
        )
        await state.update_data(
            {"nomer_8": nomer_8}
        )

        photo = open(f"./data/tavarlar/4_800/{nomer_8}.jpg", "rb")
        await call.message.answer_photo(photo=photo, caption=f"{tavar_malumotlari_800[nomer_8]}",
                                        reply_markup=mahsulotlar_inline)
        await call.message.delete()


# savatga qo'shish 1 qism
# savatga qo'shish 1 qism
# savatga qo'shish 1 qism
# savatga qo'shish 1 qism
# savatga qo'shish 1 qism
# savatga qo'shish 1 qism
# savatga qo'shish 1 qism
# savatga qo'shish 1 qism


@dp.callback_query_handler(text="dobavit_2")
async def dsfsefsf(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_8 = data.get("nomer_8")

    if nomer_8 is None:
        await call.message.delete()
    else:
        buy_soni_8 = 1
        buyurtma_inline = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="-",
                        callback_data="minus_buy_2"
                    ),
                    InlineKeyboardButton(
                        text=f"{buy_soni_8}",
                        callback_data="electronics_2"
                    ),
                    InlineKeyboardButton(
                        text="+",
                        callback_data="plus_buy_2"
                    )
                ]
            ]
        )
        await state.update_data(
            {"buy_soni_8": buy_soni_8}
        )
        await state.update_data(
            {"gr": 800}
        )
        photo1 = open(f"./data/tavarlar/4_800/{nomer_8}.jpg", "rb")
        photo2 = open(f"./data/tavarlar/4_800/{nomer_8}_2.jpg", "rb")
        photo3 = open(f"./data/tavarlar/4_800/{nomer_8}_3.jpg", "rb")
        await call.message.answer_photo(photo=photo1)
        await call.message.answer_photo(photo=photo2, reply_markup=davom_buyurtma)
        await call.message.answer_photo(photo=photo3, caption=f"{tavar_malumotlari_800[nomer_8]}\n\n"
                                                              f"<b>Miqdorni tanlang:</b>",
                                        reply_markup=buyurtma_inline)

        await call.message.delete()


@dp.callback_query_handler(lambda call: call.data == "minus_buy_2" or call.data == "plus_buy_2")
async def dsfsefsf(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    nomer_8 = data.get("nomer_8")
    buy_soni_8 = (data.get("buy_soni_8"))

    if nomer_8 is None or buy_soni_8 is None:
        await call.message.delete()
    else:

        buy_soni_8 = int(buy_soni_8)
        if buy_soni_8 == None:
            buy_soni_8 = 0
        if call.data == "plus_buy_2":
            buy_soni_8 = buy_soni_8 + 1
        else:
            buy_soni_8 = buy_soni_8 - 1

        if buy_soni_8 < 0:
            buy_soni_8 = 0
        buyurtma_inline = InlineKeyboardMarkup(
            inline_keyboard=[
                # [
                #     InlineKeyboardButton(text="Davom ettish", callback_data="buyurtma_berish_800")
                # ],
                [
                    InlineKeyboardButton(
                        text="-",
                        callback_data="minus_buy_2"
                    ),
                    InlineKeyboardButton(
                        text=f"{buy_soni_8}",
                        callback_data="electronics_2"
                    ),
                    InlineKeyboardButton(
                        text="+",
                        callback_data="plus_buy_2"
                    )
                ]
            ]
        )
        await state.update_data(
            {"buy_soni_8": buy_soni_8}
        )
        await state.update_data(
            {"gr": 800}
        )

        await call.message.edit_reply_markup(reply_markup=buyurtma_inline)
