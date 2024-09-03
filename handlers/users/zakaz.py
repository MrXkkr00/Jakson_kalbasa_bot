from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import group_id, ADMINS
from handlers.users.savat import db_tavar, tavar_dict
from handlers.users.til import db_user
from keyboards.default.contact import locatsiya
from keyboards.default.menu import dastavka, olib_ketish, vaqt_lanlash, bosh_menu, tolov_turi
from loader import dp, bot


class YetkazishState(StatesGroup):
    loco = State()
    loco_1 = State()
    loco_2 = State()
    # vaqt = State()
    # tolov = State()


@dp.message_handler(text="🏠Bosh menu", state=[YetkazishState.loco, YetkazishState.loco_1, YetkazishState.loco_2])
async def bot2132_start(message: types.Message):
    await message.delete()
    await message.answer(f"Assalomu Alaykum! ", reply_markup=bosh_menu)


@dp.message_handler(text="/start", state=[YetkazishState.loco, YetkazishState.loco_1, YetkazishState.loco_2])
async def bot2132_start(message: types.Message):
    await message.delete()
    await message.answer(f"Assalomu Alaykum! ", reply_markup=bosh_menu)


@dp.message_handler(text="🏠Bosh menu")
async def bot3242art(message: types.Message):
    await message.delete()
    await message.answer(f"Assalomu Alaykum! ", reply_markup=bosh_menu)


@dp.message_handler(text="✅Buyurtmani amalga oshirish")
async def zakaz1(message: types.Message):
    await message.answer(f"Yetkazib berish turini tanlang", reply_markup=dastavka)


@dp.message_handler(text="🏃️ Olib ketish")
async def zakaz2(message: types.Message):
    await message.delete()
    await message.answer(f"Eng yaqin filialni tanlang", reply_markup=olib_ketish)


@dp.message_handler(text="🚕 Yetkazib berish")
async def zakaz3(message: types.Message):
    await message.delete()
    await message.answer(f"Buyurtmani davom ettirish uchun manzilingizni kiriting", reply_markup=locatsiya)
    await YetkazishState.loco.set()


@dp.message_handler(content_types="location", state=YetkazishState.loco)
async def loco(message: types.Message, state: FSMContext):
    await message.answer(f"Qulay yetkazib berish vaqtini belgilang", reply_markup=vaqt_lanlash)
    # global lat, lon
    # lat = message.location.latitude
    # lon = message.location.longitude
    await state.update_data(
        {"lat": message.location.latitude}
    )
    await state.update_data(
        {"lon": message.location.longitude}
    )
    # print(message.location.latitude, message.location.longitude)
    await YetkazishState.loco_1.set()


@dp.message_handler(text="Hozir", state=YetkazishState.loco_1)
async def lo21312co(message: types.Message, state: FSMContext):

    await state.update_data(
        {"delivery_date": f"Yo'q"}
    )
    await message.answer(f"Iltimos, mahsulot uchun to'lang", reply_markup=tolov_turi)
    await YetkazishState.loco_2.set()



tavar_dict_naqt = {330:
                       {0: {1: "1. Mo'l kolbasalari - Bavariya Qadoqda - 330g",
                            2: "2. Mo'l kolbasalari ko'katlar bilan - Gatlinburg Qadoqda - 330g",
                            3: "3. Mo'l kolbasalari achchiqroq - Peperoni Qadoqda - 330g",
                            4: "4. Pishloqli Tovuqli Kolbasa - Haniken Qadoqda - 330g",
                            5: "5. Tovuq kolbasalari ko'katlar bilan - Bratwurst Qadoqda - 330g",
                            6: "6. Tovuq kolbasalari achchiqroq - Bombay Qadoqda - 330g"
                            },
                        1: 40000,
                        2: 40000,
                        3: 40000,
                        4: 35000,
                        5: 35000,
                        6: 35000},
                   800:
                       {0: {1: "Inglizcha Seriya  Qadoqda: - 400g Pishloqli Tovuqli Kolbasa "
                               "- 400g Mol Go'shtli Kolbasa",
                            2: "Italyancha Kolleksiya Qadoqda: - 400g Ko'katli Tovuqli  Kolbasa "
                               "- 400g Ko'katli Mol Go'shtli Kolbasa",
                            3: "Meksikancha Duet Qadoqda: - 400g Achchiq Tovuqli Kolbasa "
                               "- 400g Achchiq Mol Go'shtli Kolbasa",
                            4: "Fransuzcha Simfoniya Qadoqda: - 400g Pishloqli Mol Go'shtli Kolbasa "
                               "- 400g Qo'zichoq Go'shtli Kolbasa"
                            },
                        1: 85000,
                        2: 85000,
                        3: 85000,
                        4: 90000}
                   }


@dp.message_handler(text="💵Naqd to'lash", state=YetkazishState.loco_2)
async def lo21312co(message: types.Message, state: FSMContext):
    await message.delete()
    try:
        await db_tavar.create()
    except:
        pas = 1

    tavar = await db_tavar.select_Tavar(user_id=str(message.from_user.id))
    await db_tavar.delete_Tavar(user_id=str(message.from_user.id))

    summa = 0

    await db_tavar.disconnect()
    tavar_text = ""
    for i in range(len(tavar)):
        tavar_text = tavar_text + f"🛍{tavar_dict_naqt[int(tavar[i][2])][0][int(tavar[i][3])]}\n" \
                     + f"Maxsulot soni: {tavar[i][4]}\n" \
                     + f"💵Narxi: {int(tavar[i][5]) * int(tavar[i][4])}\n\n"

        summa = summa + int(tavar[i][5]) * int(tavar[i][4])
    if summa == 0:
        await message.answer(f"Sizda hali buyutmalar mavjud emas.", reply_markup=bosh_menu)
    else:
        tavar_text = tavar_text + f"💵Umumiy summa : <b>{summa}</b>\n"

        await message.answer(tavar_text)

        try:
            await db_user.create()
            user = await db_user.select_user(user_id=str(message.from_user.id))

        except:
            user = None
            await bot.send_message(ADMINS[0], f"Xato zakaz.py lo21312co")
        finally:
            await db_user.disconnect()
        name = user[3]
        nomer = user[4]
        soat = str((int(strftime('%H', gmtime())) + 5) % 24) + f":{str(strftime('%M', gmtime()))}"
        vaqt = str(strftime(f"%d/%m/%Y", gmtime()))

        data = await state.get_data()

        delivery_date = data.get("delivery_date")

        await bot.send_message(group_id, f"<b>🙋🏻‍♂️Mijoz :</b> {name}\n"
                                               f"<b>📕Username :</b> @{message.from_user.username}\n"
                                               f"<b>📲Nomer :</b>  {nomer}\n"
                                               f"<b>⏱Vaqt :</b> {soat} {vaqt} \n"
                                               f"<b>⏱Yetkazish Vaqti :</b> {delivery_date} \n"
                                               f"<b>💵Naxt </b> \n"
                                               f"<b>📦Yetkazib berish</b>\n\n"
                                               f"{tavar_text}")
        try:
            data = await state.get_data()
            lat = data.get("lat")
            lon = data.get("lon")
            lon = data.get("lon")

            await bot.send_location(chat_id=group_id, latitude=lat, longitude=lon)

        except:
            pas = 1
    await message.answer(f"✅Buyurtmangiz muvaffaqiyatli qabul qilindi. Operator javobini kutishingiz shart emas.",
                         reply_markup=bosh_menu)
    await state.storage.reset_data(chat=message.chat.id, user=message.from_user.id)
    await state.finish()
