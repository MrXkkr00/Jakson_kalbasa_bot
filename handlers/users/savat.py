from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu import bosh_menu, buyutma, tavarlar
from loader import dp, bot
from utils.db_api.tavar_sql import Database_Tavar
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging

db_tavar = Database_Tavar()

tavar_dict = {330:
                  {0: {1: "1. Mo'l kolbasalari - Bavariya\nQadoqda - 330g\n\n40,000 UZS/dana",
                       2: "2. Mo'l kolbasalari ko'katlar bilan - Gatlinburg\nQadoqda - 330g\n\n40,000 UZS/dana",
                       3: "3. Mo'l kolbasalari achchiqroq - Peperoni\nQadoqda - 330g\n\n40,000 UZS/dana",
                       4: "4. Pishloqli Tovuqli Kolbasa - Haniken\nQadoqda - 330g\n\n35,000 UZS/dana",
                       5: "5. Tovuq kolbasalari ko'katlar bilan - Bratwurst\nQadoqda - 330g\n\n35,000 UZS/dana",
                       6: "6. Tovuq kolbasalari achchiqroq - Bombay\nQadoqda - 330g\n\n35,000 UZS/dana"
                       },
                   1: 40000,
                   2: 40000,
                   3: 40000,
                   4: 35000,
                   5: 35000,
                   6: 35000},
              800:
                  {0: {1: "Inglizcha Seriya\n Qadoqda:\n\n- 400g Pishloqli Tovuqli Kolbasa\n"
                          "- 400g Mol Go'shtli Kolbasa\n\n85,000 UZS/dana",
                       2: "Italyancha Kolleksiya\nQadoqda:\n\n- 400g Ko'katli Tovuqli  Kolbasa\n"
                          "- 400g Ko'katli Mol Go'shtli Kolbasa\n\n85,000 UZS/dana",
                       3: "Meksikancha Duet\nQadoqda:\n\n- 400g Achchiq Tovuqli Kolbasa\n"
                          "- 400g Achchiq Mol Go'shtli Kolbasa\n\n85,000 UZS/dana",
                       4: "Fransuzcha Simfoniya\nQadoqda:\n\n- 400g Pishloqli Mol Go'shtli Kolbasa\n"
                          "- 400g Qo'zichoq Go'shtli Kolbasa\n\n90,000 UZS/dana"
                       },
                   1: 85000,
                   2: 85000,
                   3: 85000,
                   4: 90000}
              }


@dp.message_handler(text="🛒Savat")
async def savat1(message: types.Message):
    try:
        await db_tavar.create()
    except:
        pas = 1


    tavar = await db_tavar.select_Tavar(user_id=str(message.from_user.id))

    summa = 0

    await db_tavar.disconnect()
    for i in range(len(tavar)):
        await message.answer(f"🛍{tavar_dict[int(tavar[i][2])][0][int(tavar[i][3])]}\n\n"
                             f"Maxsulot soni: {tavar[i][4]}\n"
                             f"💵Narxi: {int(tavar[i][5]) * int(tavar[i][4])}")
        summa = summa + int(tavar[i][5]) * int(tavar[i][4])
    if summa == 0:
        await message.answer(f"Sizda hali buyutmalar mavjud emas.", reply_markup=bosh_menu)
    else:

        await message.answer(f"💵Umumiy summa : <b>{summa}</b>\n"
                             f"Kerakli bo'limni tanlang", reply_markup=buyutma)


@dp.message_handler(text="Savatga qo'shish")
async def dsfsefsf_ru(message: types.Message, state: FSMContext):
    data = await state.get_data()
    gr = data.get("gr")

    if gr == 330:
        nomer_s = data.get("nomer_3")
        buy_soni_s = (data.get("buy_soni_3"))
    else:
        nomer_s = data.get("nomer_8")
        buy_soni_s = (data.get("buy_soni_8"))

    try:
        await db_tavar.create()
    except:
        pas = 1

    await db_tavar.add_Tavar(
        user_id=str(message.from_user.id),
        t_turi=str(gr), t_nomer=str(nomer_s),
        t_soni=str(buy_soni_s),
        t_narxi=str(tavar_dict[gr][nomer_s])
    )
    
    tavar = await db_tavar.select_Tavar(user_id=str(message.from_user.id))



    summa = 0
    for i in range(len(tavar)):
        await message.answer(f"🛍{tavar_dict[int(tavar[i][2])][0][int(tavar[i][3])]}\n\n"
                             f"Maxsulot soni: {tavar[i][4]}\n"
                             f"💵Narxi: {int(tavar[i][5]) * int(tavar[i][4])}")
        summa = summa + int(tavar[i][5]) * int(tavar[i][4])

    await db_tavar.disconnect()

    if summa == 0:
        await message.answer(f"Sizda hali buyutmalar mavjud emas.", reply_markup=bosh_menu)
    else:
        await message.answer(f"💵Umumiy summa : <b>{summa}</b>\n"
                             f"Kerakli bo'limni tanlang", reply_markup=buyutma)




@dp.message_handler(text="🔄Savatni tozalash")
async def savat23(message: types.Message):
    try:
        await db_tavar.create()
    except:
        pas = 1

    try:
        await db_tavar.delete_Tavar(user_id=str(message.from_user.id))
        await message.answer("Savat tozalandi.", reply_markup=bosh_menu)

    except Exception as e:
        logging.error(f"Error deleting items: {e}")
        await bot.send_message(chat_id=7010118152, text="Savatni tozalashda xatolik yuz berdi.")
    finally:
        await db_tavar.disconnect()


@dp.message_handler(text="📝Buyurtma qo'shish")
async def main1(message: types.Message):
    await message.answer(f"Tavarlar", reply_markup=tavarlar)
