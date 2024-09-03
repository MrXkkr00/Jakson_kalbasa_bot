from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.contact import contact_keyboard
from keyboards.default.menu import bosh_menu
# from keyboards.default.Keyboards import bosh_menu, contact_keyboard
from loader import dp
from utils.db_api.users_sql import Database_User


# from utils.db_api.users_sql import Database_User


class Qabul_State(StatesGroup):
    ism = State()
    contact = State()


@dp.message_handler(state=Qabul_State.ism)
async def qabul2(message: types.Message, state: FSMContext):
    await state.update_data(
        {"ism": message.text}
    )
    await message.answer(f"Kontaktizni yuboring : ", reply_markup=contact_keyboard)
    await Qabul_State.next()


@dp.message_handler(content_types="contact", state=Qabul_State.contact)
async def qabul3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = (str(message.from_user.id))
    user_name = message.from_user.username
    fullname = data.get("ism")
    phone_number = message.contact.phone_number
    db_user = Database_User()
    try:
        await db_user.create()
    except:
        pas = 1

    await db_user.add_user(user_id=user_id, user_name=user_name, name=fullname, phone_nomer=str(phone_number))

    await message.answer(f"{fullname}\n{phone_number}\nSiz ro'yxatga olindingiz: ", reply_markup=bosh_menu)
    await state.finish()
