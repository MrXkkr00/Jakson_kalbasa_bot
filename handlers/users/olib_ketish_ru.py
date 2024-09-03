import math
from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import ADMINS, group_id
from handlers.users.functions import yaqin_location_fun
from handlers.users.savat import db_tavar
from handlers.users.til import db_user
from keyboards.default.contact import locatsiya_ru
from keyboards.default.menu_ru import olib_ketish_ru, bosh_menu_ru
from loader import dp, bot


class LocoYaqinState_ru(StatesGroup):
    loco = State()


@dp.message_handler(text="🏠Главное меню", state=[LocoYaqinState_ru.loco])
async def locobosh_menu_ru(message: types.Message, state:FSMContext):
    await message.delete()
    await message.answer(f"Привет! ", reply_markup=bosh_menu_ru)
    await state.finish()


tavar_dict_naqt_ru = {330:
                          {0: {1: "1.Колбаски Говяжьи - Баварские\nВ упаковке - 330г",
                               2: "2. Колбаски Говяжьи с Зеленью - Гатлинбург\nВ упаковке - 330г",
                               3: "3. Колбаски Говяжьи Пикантные - Пеперони\nВ упаковке - 330г",
                               4: "4. Колбаски Куриные с Сыром - Ханикен\nВ упаковке - 330г",
                               5: "5. Колбаски Куриные с Зеленью - Братвурст\nВ упаковке - 330г",
                               6: "6. Колбаски Куриные Пикантные - Бомбей\nВ упаковке - 330г"
                               },
                           1: 40000,
                           2: 40000,
                           3: 40000,
                           4: 35000,
                           5: 35000,
                           6: 35000},
                      800:
                          {0: {1: "1. Английская Серия\nВ упаковке:\n\n- 400г Колбасок Куриных с Сыром\n"
                               "- 400г Колбасок Говяжьих",
                            2: "2. Итальянская Коллекция\nВ упаковке:\n\n- 400г Колбасок Куриных с Зеленью\n"
                               "- 400г Колбасок Говяжьих с Зеленью",
                            3: "3. Мексиканский Дуэт\nВ упаковке:\n\n- 400г Колбасок Куриных Острых\n"
                               "- 400г Колбасок Говяжьих Острых",
                            4: "4. Французская Симфония\nВ упаковке:\n\n- 400г Колбасок 'Говяжьи с Сыром'\n"
                               "- 400г Колбасок 'из Баранины'"
                            },
                           1: 85000,
                           2: 85000,
                           3: 85000,
                           4: 90000}
                      }


# 1
@dp.message_handler(text=["Госпитальный Рынок", "Рынок Катартал", "Рынок Аския", "Фархадский Рынок",
                          "Буз Базар", "Рынок Чимган", "Рынок Сергели (Дех)", "Рынок Кадышева"])
async def boafsfsa_ru(message: types.Message):
    if message.text == 'Госпитальный Рынок':
        # 1
        text = f'Рынок Госпитальный. Вывеска "PROMEAT"\n' \
               f'+998903474655\n\nВ данный момент филиал:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Работает</b>  \nРабочее время: 8:00-18:00\n'
        else:
            text += f'<b>Не работает</b>  \nРабочее время:: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.291183, longitude=69.274846)

    if message.text == "Рынок Катартал":
        # 2
        text = f'Рынок Катартал. Магазины 59, 92. Вывески "Классный Колбасный"\n' \
               f'+998903474655\n\nВ данный момент филиал:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Работает</b>  \nРабочее время: 8:00-18:00\n'
        else:
            text += f'<b>Не работает</b>  \nРабочее время:: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.291333, longitude=69.210063)

    if message.text == "Рынок Аския":
        # 3
        text = f'Рынок Аския.  Вывеска "Колбасная Лавка".\n' \
               f'+998903474655\n\nВ данный момент филиал:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Работает</b>  \nРабочее время: 8:00-18:00\n'
        else:
            text += f'<b>Не работает</b>  \nРабочее время:: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.283508, longitude=69.250255)

    if message.text == "Фархадский Рынок":
        # 4
        text = f"Фархадский Рынок.\n" \
               f'+998903474655\n\nВ данный момент филиал:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Работает</b>  \nРабочее время: 8:00-18:00\n'
        else:
            text += f'<b>Не работает</b>  \nРабочее время:: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.285870, longitude=69.189906)

    if message.text == "Буз Базар":

        # 5
        text = f"Буз Базар.\n" \
               f'+998903474655\n\nВ данный момент филиал:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Работает</b>  \nРабочее время: 8:00-18:00\n'
        else:
            text += f'<b>Не работает</b>  \nРабочее время:: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.328183, longitude=69.325687)

    if message.text == "Рынок Чимган":
        # 6
        text = f"Рынок Чимган.\n" \
               f'+998903474655\n\nВ данный момент филиал:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Работает</b>  \nРабочее время: 8:00-18:00\n'
        else:
            text += f'<b>Не работает</b>  \nРабочее время:: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.347753, longitude=69.346595)

    if message.text == "Рынок Сергели (Дех)":
        # 7
        text = f"Рынок Сергели (Дех).\n" \
               f'+998903474655\n\nВ данный момент филиал:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Работает</b>  \nРабочее время: 8:00-18:00\n'
        else:
            text += f'<b>Не работает</b>  \nРабочее время:: 8:00-18:00'

        await message.answer(text)
        await message.answer_location(latitude=41.226840, longitude=69.218662)

    if message.text == "Рынок Кадышева":
        # 8
        text = f"Рынок Кадышева.\n" \
               f'+998903474655\n\nВ данный момент филиал:   '
        soat = (int(strftime('%H', gmtime())) + 5) % 24

        if soat >= 8 and soat < 18:
            text += f'<b>Работает</b>  \nРабочее время: 8:00-18:00\n'
        else:
            text += f'<b>Не работает</b>  \nРабочее время:: 8:00-18:00'

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
        tavar_text = tavar_text + f"🛍{tavar_dict_naqt_ru[int(tavar[i][2])][0][int(tavar[i][3])]}\n" \
                     + f"Количество продукта: {tavar[i][4]}\n" \
                     + f"💵Расходы: {int(tavar[i][5]) * int(tavar[i][4])}\n\n"

        summa = summa + int(tavar[i][5]) * int(tavar[i][4])
    if summa == 0:
        await message.answer(f"У вас пока нет размеров.", reply_markup=bosh_menu_ru)
    else:
        tavar_text = tavar_text + f"💵Общая сумма : <b>{summa}</b>\n"

        await message.answer(tavar_text)

        try:
            await db_user.create()
            user = await db_user.select_user(user_id=str(message.from_user.id))

        except:
            user = None
            await bot.send_message(ADMINS[0], f"Xato olib_ketish_ru.py page 206")
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

    await message.answer(f"✅Ваш заказ успешно получен. \n"
                         f'📝 Вы можете забрать свой заказ в отделении {message.text}.',  reply_markup=bosh_menu_ru)


@dp.message_handler(text="📍 Определить ближайший филиал")
async def location_yaqin_ru(message: types.Message):
    await message.answer(f"Отправьте свое местоположение", reply_markup=locatsiya_ru)
    await LocoYaqinState_ru.loco.set()


@dp.message_handler(content_types='location', state=LocoYaqinState_ru.loco)
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
        yaqin_loc = "Рынок Аския"

    if natija == joy_4:
        yaqin_loc = "Фархадский Рынок"

    if natija == joy_5:
        yaqin_loc = "Буз Базар"

    if natija == joy_6:
        yaqin_loc = "Рынок Чимган"

    if natija == joy_7:
        yaqin_loc = "Рынок Сергели (Дех)"

    if natija == joy_8:
        yaqin_loc = "Рынок Кадышева"
    await message.answer(f"Наш ближайший филиал для вас:\n\n"
                         f"<b>{yaqin_loc}</b>", reply_markup=olib_ketish_ru)

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



#
# @dp.message_handler(content_types='location')
# async def location_def(message: types.Message):
#     print(1)
#     lat = message.location.latitude
#     lon = message.location.longitude
#     print(lat)
#     print(lon)
#     await message.answer(f"{lat}\n{lon}")
