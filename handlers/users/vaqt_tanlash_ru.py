from time import strftime, gmtime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery

from handlers.users.zakaz_ru import YetkazishState_ru
from keyboards.default.menu_ru import tolov_turi_ru, bosh_menu_only_ru
from keyboards.default.vaqt_tanlash import oy_10_ru, oy_1_ru, oy_2_ru, oy_3_ru, oy_4_ru, oy_5_ru, oy_6_ru, oy_7_ru, oy_8_ru, oy_9_ru, oy_11_ru, oy_12_ru, \
    kun, soat_hammasi
from loader import dp, bot


# state = YetkazishState.loco_1

@dp.message_handler(text="На Время", state=YetkazishState_ru.loco_1)
async def lo21312co(message: types.Message):
    await message.answer(f"Выберите удобное для вас время.", reply_markup=bosh_menu_only_ru)
    oy_son = int(strftime(f"%m", gmtime()))
    oy_keyboard = oy_10_ru
    if oy_son == 1:
        oy_keyboard = oy_1_ru
    if oy_son == 2:
        oy_keyboard = oy_2_ru
        oy_keyboard2 = oy_3_ru
    if oy_son == 3:
        oy_keyboard = oy_3_ru
        oy_keyboard2 = oy_4_ru
    if oy_son == 4:
        oy_keyboard = oy_4_ru
        oy_keyboard2 = oy_5_ru
    if oy_son == 5:
        oy_keyboard = oy_5_ru
        oy_keyboard2 = oy_6_ru
    if oy_son == 6:
        oy_keyboard = oy_6_ru
        oy_keyboard2 = oy_7_ru
    if oy_son == 7:
        oy_keyboard = oy_7_ru
        oy_keyboard2 = oy_8_ru
    if oy_son == 8:
        oy_keyboard = oy_8_ru
        oy_keyboard2 = oy_9_ru
    if oy_son == 9:
        oy_keyboard = oy_9_ru
        oy_keyboard2 = oy_10_ru
    if oy_son == 10:
        oy_keyboard = oy_10_ru
        oy_keyboard2 = oy_11_ru
    if oy_son == 11:
        oy_keyboard = oy_11_ru
        oy_keyboard2 = oy_12_ru
    if oy_son == 12:
        oy_keyboard = oy_12_ru
        oy_keyboard2 = oy_1_ru
    await message.answer(f"Выберите месяц", reply_markup=oy_keyboard)
    # await message.answer(f"Oyni tanlang", reply_markup=oy_keyboard2)



@dp.callback_query_handler(text_contains="0000", state=YetkazishState_ru.loco_1)
async def buy_courses_ru(call: CallbackQuery, state: FSMContext):
    callback_data = call.data
    await call.message.delete()
    oy1 = int(int(callback_data) / 10000)
    await state.update_data(
        {"oy": oy1}
    )
    await call.message.answer("Выберите день", reply_markup=kun)


@dp.callback_query_handler(text_contains="99", state=YetkazishState_ru.loco_1)
async def buy_courses_ru(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    callback_data = call.data
    kun1 = int(int(callback_data) / 100)
    await state.update_data(
        {"kun": kun1}
    )
    await call.message.answer("Выберите час", reply_markup=soat_hammasi)


@dp.callback_query_handler(text_contains="*", state=YetkazishState_ru.loco_1)
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
    await call.message.answer(f"Срок доставки вашего заказа \n"
                              f"⏱<b>{delivery_date}</b>")
    await call.message.answer(f"Пожалуйста оплатите продукт", reply_markup=tolov_turi_ru)
    await YetkazishState_ru.loco_2.set()
