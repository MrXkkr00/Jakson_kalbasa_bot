from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS, group_id
from handlers.users.functions import click_uchun_fun
from handlers.users.olib_ketish_ru import tavar_dict_naqt_ru
from handlers.users.savat import db_tavar
from handlers.users.til import db_user
from handlers.users.zakaz_ru import YetkazishState_ru
from keyboards.default.menu_ru import bosh_menu_ru
from loader import dp, bot


@dp.message_handler(text="💳Оплатить через Click", state=YetkazishState_ru.loco_2)
async def fads_ru(message: types.Message, state: FSMContext):
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
            await bot.send_message(ADMINS[0], f"Xato tolov_click_ru.py fads_ru page 49")
        finally:
            await db_user.disconnect()
        name = user[3]
        nomer = user[4]
        soat = str((int(strftime('%H', gmtime())) + 5) % 24) + f":{str(strftime('%M', gmtime()))}"
        vaqt = str(strftime(f"%d/%m/%Y", gmtime()))

        nomer_click = user[4][-12:]
        summa_click = summa

        invoice = click_uchun_fun(nomer_click, summa_click)
        data = await state.get_data()
        delivery_date = data.get("delivery_date")

        await bot.send_message(group_id, f"<b>🙋🏻‍♂️Mijoz :</b> {name}\n"
                                         f"<b>📕Username :</b> @{message.from_user.username}\n"
                                         f"<b>📲Nomer :</b>  {nomer}\n"
                                         f"<b>⏱Vaqt :</b> {soat} {vaqt} \n"
                                         f"<b>⏱Yetkazish Vaqti :</b> {delivery_date} \n"
                                         f"<b>💳Click </b> \n"
                                         f"<b>Invoice: {invoice} </b> \n"
                                         f"<b>📦Yetkazib berish</b>\n\n"
                                         f"{tavar_text}")
        try:
            data = await state.get_data()
            lat = data.get("lat")
            lon = data.get("lon")

            await bot.send_location(chat_id=group_id, latitude=lat, longitude=lon)

        except:
            pas = 1
    await message.answer(f"✅Ваш заказ успешно принят. Не ждите ответа оператора..",
                         reply_markup=bosh_menu_ru)
    await message.answer(f"Счет отправлен на номер вашего счета\n"
                         f"Вы можете произвести оплату через мобильное приложение Click, бота Telegram или 880.")
    await state.storage.reset_data(chat=message.chat.id, user=message.from_user.id)
    await state.finish()
