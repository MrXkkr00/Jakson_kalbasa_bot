import math
from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import ADMINS, group_id
from handlers.users.functions import yaqin_location_fun
from handlers.users.savat import db_tavar
from handlers.users.til import db_user
from keyboards.default.contact import locatsiya
from keyboards.default.menu import olib_ketish, bosh_menu
from loader import dp, bot


class LocoYaqinState(StatesGroup):
    loco = State()


@dp.message_handler(text="🏠Bosh menu", state=LocoYaqinState.loco)
async def locobosh_menu(message: types.Message):
    await message.delete()
    await message.answer(f"Assalomu Alaykum! ", reply_markup=bosh_menu)


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


# 1
@dp.message_handler(text=["Kasalxona bozori", "Qatortol bozori", "Askiya bozori", "Farxod bozori",
                          "Buz bozori", "Chimgan bozori", "Sergili (Dehqon) bozori", "Qadsheva bozori"])
async def boafsfsa(message: types.Message):
    if message.text == 'Kasalxona bozori':
        # 1
        text = f'Kasalxona bozori. "PROMEAT" belgisi\n' \
               f'+998903474655\n\nHozirda filial:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
        else:
            text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.291183, longitude=69.274846)

    if message.text == "Qatortol bozori":
        # 2
        text = f"Katartal bozori. 59, 92-do'konlar.'Salqin kolbasa' belgilari\n" \
               f'+998903474655\n\nHozirda filial:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
        else:
            text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.291333, longitude=69.210063)

    if message.text == "Askiya bozori":
        # 3
        text = f"Askiya bozori.\n" \
               f'+998903474655\n\nHozirda filial:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
        else:
            text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.283508, longitude=69.250255)

    if message.text == "Farxod bozori":
        # 4
        text = f"Farhod bozori.\n" \
               f'+998903474655\n\nHozirda filial:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
        else:
            text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.285870, longitude=69.189906)

    if message.text == "Buz bozori":

        # 5
        text = f"Buz bozori.\n" \
               f'+998903474655\n\nHozirda filial:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
        else:
            text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.328183, longitude=69.325687)

    if message.text == "Chimgan bozori":
        # 6
        text = f"Chimgan bozori.\n" \
               f'+998903474655\n\nHozirda filial:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
        else:
            text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.347753, longitude=69.346595)

    if message.text == "Sergili (Dehqon) bozori":
        # 7
        text = f"Sergeli Dehqon  bozori.\n" \
               f'+998903474655\n\nHozirda filial:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
        else:
            text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.226840, longitude=69.218662)

    if message.text == "Qadsheva bozori":
        # 8
        text = f"Qadsheva bozori.\n" \
               f'+998903474655\n\nHozirda filial:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
        else:
            text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.285459, longitude=69.348460)

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
            await bot.send_message(ADMINS[0], f"Xato olib ketish uz.py page 213")
        finally:
            await db_user.disconnect()
        name = user[3]
        nomer = user[4]
        soat = str((int(strftime('%H', gmtime())) + 5) % 24) + f":{str(strftime('%M', gmtime()))}"
        vaqt = str(strftime(f"%d/%m/%Y", gmtime()))

        await bot.send_message(group_id, f"<b>🙋🏻‍♂️Mijoz :</b> {name}\n"
                                         f"<b>📕Username :</b> @{message.from_user.username}\n"
                                         f"<b>📲Nomer :</b>  {nomer}\n"
                                         f"<b>⏱Vaqt :</b> {soat} {vaqt} \n"
                                         f"<b>📦olib ketish</b>\n"
                                         f'<b>📍filial:  "{message.text}"</b> \n\n'
                                         f"{tavar_text}")

    await message.answer(f"✅Buyurtmangiz muvaffaqiyatli qabul qilindi. \n"
                         f'📝 Buyurtmangizni  "{message.text}" '
                         f"filialidan olib ketishingiz mumkin.",
                         reply_markup=bosh_menu)


@dp.message_handler(text="📍 Eng yaqin filialni topish")
async def location_yaqin(message: types.Message):
    await message.answer(f"O'z joylashuvingizni yuboring", reply_markup=locatsiya)
    await LocoYaqinState.loco.set()


@dp.message_handler(content_types='location', state=LocoYaqinState.loco)
async def loco2_yaqin(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    joy_1 = yaqin_location_fun(lat, lon, 41.291183, 69.274846)

    joy_2 = yaqin_location_fun(lat, lon, 41.291333, 69.210063)

    joy_3 = yaqin_location_fun(lat, lon, 41.283508, 69.250255)

    joy_4 = yaqin_location_fun(lat, lon, 41.285870, 69.189906)

    joy_5 = yaqin_location_fun(lat, lon, 41.328183, 69.325687)

    joy_6 = yaqin_location_fun(lat, lon, 41.347753, 69.346595)

    joy_7 = yaqin_location_fun(lat, lon, 41.226840, 69.218662)

    joy_8 = yaqin_location_fun(lat, lon, 41.285459, 69.348460)

    natija = min(joy_1, joy_2, joy_3, joy_4, joy_5, joy_6, joy_7, joy_8)
    yaqin_loc = ''
    if natija == joy_1:
        yaqin_loc = "Kasalxona bozori"

    if natija == joy_2:
        yaqin_loc = "Qatortol bozori"

    if natija == joy_3:
        yaqin_loc = "Askiya bozori"

    if natija == joy_4:
        yaqin_loc = "Farxod bozori"

    if natija == joy_5:
        yaqin_loc = "Askiya bozori"

    if natija == joy_6:
        yaqin_loc = "Chimgan bozori"

    if natija == joy_7:
        yaqin_loc = "Sergili (Dehqon) bozori"

    if natija == joy_8:
        yaqin_loc = "Qadsheva bozori"
    await message.answer(f"Siz uchun eng yaqin filialimiz:\n\n"
                         f"<b>{yaqin_loc}</b>", reply_markup=olib_ketish)

    await state.finish()


# 2
# @dp.message_handler(text="Qatortol bozori")
# async def boafwaewdssfsa(message: types.Message):
#     text = f"Katartal bozori. 59, 92-do'konlar.'Salqin kolbasa' belgilari\n" \
#            f'+998903474655\n\nHozirda filial:   '
#     soat = (int(strftime('%H', gmtime())) + 5) % 24
#
#     if soat >= 8 and soat < 18:
#         text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
#     else:
#         text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'
#
#     await message.answer(text)
#     await message.answer_location(latitude=41.291333, longitude=69.210063)


# 3
# @dp.message_handler(text="Askiya bozori")
# async def boafwaewdssfsa(message: types.Message):
#     text = f"Askiya bozori.\n" \
#            f'+998903474655\n\nHozirda filial:   '
#     soat = (int(strftime('%H', gmtime())) + 5) % 24
#
#     if soat >= 8 and soat < 18:
#         text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
#     else:
#         text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'
#
#     await message.answer(text)
#     await message.answer_location(latitude=41.283508, longitude=69.250255)
#

# 4
# @dp.message_handler(text="Farxod bozori")
# async def boafwaewdssfsa(message: types.Message):
#     text = f"Farhod bozori.\n" \
#            f'+998903474655\n\nHozirda filial:   '
#     soat = (int(strftime('%H', gmtime())) + 5) % 24
#
#     if soat >= 8 and soat < 18:
#         text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
#     else:
#         text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'
#
#     await message.answer(text)
#     await message.answer_location(latitude=41.285870, longitude=69.189906)
#

# 5
# @dp.message_handler(text="Buz bozori")
# async def boafwaewdssfsa(message: types.Message):
#     text = f"Buz bozori.\n" \
#            f'+998903474655\n\nHozirda filial:   '
#     soat = (int(strftime('%H', gmtime())) + 5) % 24
#
#     if soat >= 8 and soat < 18:
#         text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
#     else:
#         text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'
#
#     await message.answer(text)
#     await message.answer_location(latitude=41.328183, longitude=69.325687)


# 6
# @dp.message_handler(text="Chimgan bozori")
# async def boafwaewdssfsa(message: types.Message):
#     text = f"Chimgan bozori.\n" \
#            f'+998903474655\n\nHozirda filial:   '
#     soat = (int(strftime('%H', gmtime())) + 5) % 24
#
#     if soat >= 8 and soat < 18:
#         text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
#     else:
#         text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'
#
#     await message.answer(text)
#     await message.answer_location(latitude=41.347753, longitude=69.346595)


# 7
# @dp.message_handler(text="Sergili (Dehqon) bozori")
# async def boafwaewdssfsa(message: types.Message):
#     text = f"Sergeli Dehqon  bozori.\n" \
#            f'+998903474655\n\nHozirda filial:   '
#     soat = (int(strftime('%H', gmtime())) + 5) % 24
#
#     if soat >= 8 and soat < 18:
#         text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
#     else:
#         text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'
#
#     await message.answer(text)
#     await message.answer_location(latitude=41.226840, longitude=69.218662)


# 8
# @dp.message_handler(text="Qadsheva bozori")
# async def boafwaewdssfsa(message: types.Message):
#     text = f"Qadsheva bozori.\n" \
#            f'+998903474655\n\nHozirda filial:   '
#     soat = (int(strftime('%H', gmtime())) + 5) % 24
#
#     if soat >= 8 and soat < 18:
#         text += f'<b>Ishlayapdi</b>  \nish vaqti: 8:00-18:00\n'
#     else:
#         text += f'<b>Ishlamayapdi</b>  \nish vaqti: 8:00-18:00'
#
#     await message.answer(text)
#     await message.answer_location(latitude=41.285459, longitude=69.348460)


@dp.message_handler(text="📍 Eng yaqin filialni topish")
async def location_yaqin(message: types.Message):
    await message.answer(f"O'z joylashuvingizni yuboring", reply_markup=locatsiya)
    await LocoYaqinState.loco.set()


@dp.message_handler(content_types='location', state=LocoYaqinState.loco)
async def loco2_yaqin(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    joy_1 = yaqin_location_fun(lat, lon, 41.291183, 69.274846)

    joy_2 = yaqin_location_fun(lat, lon, 41.291333, 69.210063)

    joy_3 = yaqin_location_fun(lat, lon, 41.283508, 69.250255)

    joy_4 = yaqin_location_fun(lat, lon, 41.285870, 69.189906)

    joy_5 = yaqin_location_fun(lat, lon, 41.328183, 69.325687)

    joy_6 = yaqin_location_fun(lat, lon, 41.347753, 69.346595)

    joy_7 = yaqin_location_fun(lat, lon, 41.226840, 69.218662)

    joy_8 = yaqin_location_fun(lat, lon, 41.285459, 69.348460)

    natija = min(joy_1, joy_2, joy_3, joy_4, joy_5, joy_6, joy_7, joy_8)
    yaqin_loc = ''
    if natija == joy_1:
        yaqin_loc = "Kasalxona bozori"

    if natija == joy_2:
        yaqin_loc = "Qatortol bozori"

    if natija == joy_3:
        yaqin_loc = "Askiya bozori"

    if natija == joy_4:
        yaqin_loc = "Farxod bozori"

    if natija == joy_5:
        yaqin_loc = "Askiya bozori"

    if natija == joy_6:
        yaqin_loc = "Chimgan bozori"

    if natija == joy_7:
        yaqin_loc = "Sergili (Dehqon) bozori"

    if natija == joy_8:
        yaqin_loc = "Qadsheva bozori"
    await message.answer(f"Siz uchun eng yaqin filialimiz:\n\n"
                         f"<b>{yaqin_loc}</b>", reply_markup=olib_ketish)

    await state.finish()

#
# @dp.message_handler(content_types='location')
# async def location_def(message: types.Message):
#     print(1)
#     lat = message.location.latitude
#     lon = message.location.longitude
#     print(lat)
#     print(lon)
#     await message.answer(f"{lat}\n{lon}")
