from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu_ru import bosh_menu_ru, buyutma_ru, tavarlar_ru
from loader import dp
from utils.db_api.tavar_sql import Database_Tavar

db_tavar = Database_Tavar()

tavar_dict_ru = {330:
                     {0: {1: "1.Колбаски Говяжьи - Баварские\nВ упаковке - 330г\n\n40,000 сум/шт",
                          2: "2. Колбаски Говяжьи с Зеленью - Гатлинбург\nВ упаковке - 330г\n\n40,000 сум/шт",
                          3: "3. Колбаски Говяжьи Пикантные - Пеперони\nВ упаковке - 330г\n\n40,000 сум/шт",
                          4: "4. Колбаски Куриные с Сыром - Ханикен\nВ упаковке - 330г\n\n35,000 сум/шт",
                          5: "5. Колбаски Куриные с Зеленью - Братвурст\nВ упаковке - 330г\n\n35,000 сум/шт",
                          6: "6. Колбаски Куриные Пикантные - Бомбей\nВ упаковке - 330г\n\n35,000 сум/шт"
                          },
                      1: 40000,
                      2: 40000,
                      3: 40000,
                      4: 35000,
                      5: 35000,
                      6: 35000},
                 800:
                     {0: {1: "1. Английская Серия\nВ упаковке:\n\n- 400г Колбасок Куриных с Сыром\n"
                               "- 400г Колбасок Говяжьих\n\n85,000 сум/шт",
                            2: "2. Итальянская Коллекция\nВ упаковке:\n\n- 400г Колбасок Куриных с Зеленью\n"
                               "- 400г Колбасок Говяжьих с Зеленью\n\n85,000 сум/шт",
                            3: "3. Мексиканский Дуэт\nВ упаковке:\n\n- 400г Колбасок Куриных Острых\n"
                               "- 400г Колбасок Говяжьих Острых\n\n85,000 сум/шт",
                            4: "4. Французская Симфония\nВ упаковке:\n\n- 400г Колбасок 'Говяжьи с Сыром'\n"
                               "- 400г Колбасок 'из Баранины'\n\n90,000 сум/шт"
                            },
                      1: 85000,
                      2: 85000,
                      3: 85000,
                      4: 90000}
                 }


@dp.message_handler(text="🛒Корзина")
async def savat1_ru(message: types.Message):
    try:
        await db_tavar.create()
    except:
        pas = 1
    # try:
    #     await db_tavar.create_table_tavar()
    # except:
    #     pas = 1

    user = await db_tavar.select_Tavar(user_id=str(message.from_user.id))

    summa = 0
    for i in range(len(user)):
        await message.answer(f"🛍{tavar_dict_ru[int(user[i][2])][0][int(user[i][3])]}\n\n"
                             f"Количество продукта: {user[i][4]}\n"
                             f"💵цена: {int(user[i][5]) * int(user[i][4])}")
        summa = summa + int(user[i][5]) * int(user[i][4])
    await db_tavar.disconnect()
    if summa == 0:
        await message.answer(f"У вас пока нет размеров.", reply_markup=bosh_menu_ru)
    else:

        await message.answer(f"💵Общая сумма : <b>{summa}</b>\n"
                             f"Выберите нужный раздел", reply_markup=buyutma_ru)


@dp.message_handler(text="Добавить в Корзину")
async def dsfsefsf_ru(message: types.Message, state: FSMContext):
    data = await state.get_data()
    gr_ru = data.get("gr_ru")
    if gr_ru == 330:
        nomer_s = data.get("nomer_3_ru")
        buy_soni_s = (data.get("buy_soni_3_ru"))
    else:
        nomer_s = data.get("nomer_8_ru")
        buy_soni_s = (data.get("buy_soni_8_ru"))

    try:
        await db_tavar.create()
    except:
        pas = 1

    # try:
    #     await db_tavar.create_table_tavar()
    # except:
    #     pas = 1

    await db_tavar.add_Tavar(user_id=str(message.from_user.id), t_turi=str(gr_ru), t_nomer=str(nomer_s),
                             t_soni=str(buy_soni_s), t_narxi=str(tavar_dict_ru[gr_ru][nomer_s]))

    user = await db_tavar.select_Tavar(user_id=str(message.from_user.id))

    summa = 0
    await db_tavar.disconnect()
    for i in range(len(user)):
        await message.answer(f"🛍{tavar_dict_ru[int(user[i][2])][0][int(user[i][3])]}\n\n"
                             f"Количество продукта: {user[i][4]}\n"
                             f"💵цена: {int(user[i][5]) * int(user[i][4])}")
        summa = summa + int(user[i][5]) * int(user[i][4])
    if summa == 0:
        await message.answer(f"У вас пока нет размеров.", reply_markup=bosh_menu_ru)
    else:

        await message.answer(f"💵Общая сумма : <b>{summa}</b>\n"
                             f"Выберите нужный раздел", reply_markup=buyutma_ru)




@dp.message_handler(text="🔄Очистить корзину")
async def savat23_ru(message: types.Message):
    try:
        await db_tavar.create()
    except:
        pas = 1
    await db_tavar.delete_Tavar(user_id=str(message.from_user.id))
    await message.answer(f"Корзина очищена.", reply_markup=bosh_menu_ru)


@dp.message_handler(text="📝Добавить заказ")
async def main1_ru(message: types.Message):
    await message.answer(f"Товары", reply_markup=tavarlar_ru)
