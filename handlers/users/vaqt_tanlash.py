from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery

from data.config import group_id, ADMINS
from handlers.users.savat import db_tavar, tavar_dict
from handlers.users.til import db_user
from handlers.users.zakaz import YetkazishState
from keyboards.default.contact import locatsiya
from keyboards.default.menu import bosh_menu_only, tolov_turi
from keyboards.default.vaqt_tanlash import oy_10, oy_1, oy_2, oy_3, oy_4, oy_5, oy_6, oy_7, oy_8, oy_9, oy_11, oy_12, \
    kun, soat_hammasi
from loader import dp, bot


# state = YetkazishState.loco_1

@dp.message_handler(text="Vaqtni tanlash", state=YetkazishState.loco_1)
async def lo21312co(message: types.Message):
    await message.answer(f"O'zingizga qulay vaqtni tanlang.", reply_markup=bosh_menu_only)
    oy_son = int(strftime(f"%m", gmtime()))
    oy_keyboard = oy_10
    oy_keyboard2 = oy_10
    if oy_son == 1:
        oy_keyboard = oy_1
        oy_keyboard2 = oy_2
    if oy_son == 2:
        oy_keyboard = oy_2
        oy_keyboard2 = oy_3
    if oy_son == 3:
        oy_keyboard = oy_3
        oy_keyboard2 = oy_4
    if oy_son == 4:
        oy_keyboard = oy_4
        oy_keyboard2 = oy_5
    if oy_son == 5:
        oy_keyboard = oy_5
        oy_keyboard2 = oy_6
    if oy_son == 6:
        oy_keyboard = oy_6
        oy_keyboard2 = oy_7
    if oy_son == 7:
        oy_keyboard = oy_7
        oy_keyboard2 = oy_8
    if oy_son == 8:
        oy_keyboard = oy_8
        oy_keyboard2 = oy_9
    if oy_son == 9:
        oy_keyboard = oy_9
        oy_keyboard2 = oy_10
    if oy_son == 10:
        oy_keyboard = oy_10
        oy_keyboard2 = oy_11
    if oy_son == 11:
        oy_keyboard = oy_11
        oy_keyboard2 = oy_12
    if oy_son == 12:
        oy_keyboard = oy_12
        oy_keyboard2 = oy_1
    await message.answer(f"Oyni tanlang", reply_markup=oy_keyboard)
    # await message.answer(f"Oyni tanlang", reply_markup=oy_keyboard2)



@dp.callback_query_handler(text_contains="0000", state=YetkazishState.loco_1)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    await call.message.delete()
    oy1 = int(int(callback_data) / 10000)
    await state.update_data(
        {"oy": oy1}
    )
    await call.message.answer("Kunni tanlang", reply_markup=kun)


@dp.callback_query_handler(text_contains="99", state=YetkazishState.loco_1)
async def buy_courses(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    callback_data = call.data
    kun1 = int(int(callback_data) / 100)
    await state.update_data(
        {"kun": kun1}
    )
    await call.message.answer("Soatni tanlang", reply_markup=soat_hammasi)


@dp.callback_query_handler(text_contains="*", state=YetkazishState.loco_1)
async def soat(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    soat_int = int(call.data[1:])
    soat = f"{soat_int}:00-{soat_int+1}:00"
    data = await state.get_data()
    oy = int(data.get("oy"))
    kun = int(data.get("kun"))
    delivery_date = f"{kun}/{oy}/2024   {soat}"
    await state.update_data(
        {"delivery_date": delivery_date}
    )
    await call.message.answer(f"Buyurtmagizni yetkazish vaqti \n"
                              f"⏱<b>{delivery_date}</b>")
    await call.message.answer(f"Iltimos, mahsulot uchun to'lang", reply_markup=tolov_turi)
    await YetkazishState.loco_2.set()
