from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.contact import contact_keyboard
from keyboards.default.menu_ru import bosh_menu_ru
# from keyboards.default.Keyboards import bosh_menu, contact_keyboard, bosh_menu_ru
from loader import dp
from utils.db_api.users_sql import Database_User


# from utils.db_api.users_sql import Database_User


class Qabul_State_ru(StatesGroup):
    ism = State()
    contact = State()


@dp.message_handler(state=Qabul_State_ru.ism)
async def qabul21_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        {"ism": message.text}
    )
    await message.answer(f"Отправьте свой контакт : ", reply_markup=contact_keyboard)
    await Qabul_State_ru.next()


@dp.message_handler(content_types="contact", state=Qabul_State_ru.contact)
async def qabul3_ru(message: types.Message, state: FSMContext):
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

    await message.answer(f"{fullname}\n{phone_number}\nВы зарегистрированы : ", reply_markup=bosh_menu_ru)
    await state.finish()
