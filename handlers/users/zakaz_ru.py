from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import ADMINS, group_id
from handlers.users.olib_ketish_ru import tavar_dict_naqt_ru
from handlers.users.savat import db_tavar
from handlers.users.til import db_user
from keyboards.default.contact import locatsiya_ru
from keyboards.default.menu_ru import dastavka_ru, olib_ketish_ru, bosh_menu_ru, vaqt_lanlash_ru, tolov_turi_ru
from loader import dp, bot


class YetkazishState_ru(StatesGroup):
    loco = State()
    loco_1 = State()
    loco_2 = State()


@dp.message_handler(text="🏠Главное меню",
                    state=[YetkazishState_ru.loco, YetkazishState_ru.loco_1, YetkazishState_ru.loco_2])
async def bot_s32423tart(message: types.Message):
    await message.delete()
    await message.answer(f"Привет! ", reply_markup=bosh_menu_ru)


@dp.message_handler(text="✅ Завершение заказа")
async def zakaz1_ru(message: types.Message):
    await message.answer(f"Выберите тип доставки", reply_markup=dastavka_ru)


@dp.message_handler(text="🏃️ Самовывоз")
async def zakaz2_ru(message: types.Message):
    await message.delete()
    await message.answer(f"Выберите ближайший филиал", reply_markup=olib_ketish_ru)


@dp.message_handler(text="🚕 Доставка")
async def zakaz3_ru(message: types.Message):
    await message.delete()
    await message.answer(f"Чтобы продолжить заказ, отправьте свое местоположение", reply_markup=locatsiya_ru)
    await YetkazishState_ru.loco.set()


@dp.message_handler(content_types="location", state=YetkazishState_ru.loco)
async def loco_ru(message: types.Message, state: FSMContext):
    await message.answer(f"Укажите удобное время доставки", reply_markup=vaqt_lanlash_ru)
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
    await YetkazishState_ru.loco_1.set()


@dp.message_handler(text="Ближайшее", state=YetkazishState_ru.loco_1)
async def lo21312cdfo_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"delivery_date": f"Yo'q"}
    )
    await message.answer(f"Пожалуйста оплатите продукт", reply_markup=tolov_turi_ru)
    await YetkazishState_ru.loco_2.set()


@dp.message_handler(text="💵Оплата наличными", state=YetkazishState_ru.loco_2)
async def lo21312co_ru(message: types.Message, state: FSMContext):
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
            await bot.send_message(ADMINS[0], f"Xato zakaz_ru.py lo21312co_ur")
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

            await bot.send_location(chat_id=group_id, latitude=lat, longitude=lon)

        except:
            pas = 1
    await message.answer(f"✅Ваш заказ успешно принят. Ждите ответа оператора..",
                         reply_markup=bosh_menu_ru)
    await state.storage.reset_data(chat=message.chat.id, user=message.from_user.id)
    await state.finish()
