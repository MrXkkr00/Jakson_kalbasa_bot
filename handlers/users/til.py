from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
import logging
from handlers.users.qabul import Qabul_State
from handlers.users.qabul_RU import Qabul_State_ru
from keyboards.default.menu import bosh_menu
from keyboards.default.menu_ru import bosh_menu_ru

# from keyboards.default.Keyboards import bosh_menu, bosh_menu_ru
from loader import dp, bot
from utils.db_api.users_sql import Database_User

db_user = Database_User()


@dp.message_handler(text="🇺🇿 O'zbek")
async def bot_stwsasart(message: types.Message):
    user_id = (str(message.from_user.id))
    try:
        await db_user.create()
    except:
        pas = 1

    try:
        await db_user.create()
        user = await db_user.select_user(user_id=user_id)
    except:
        await bot.send_message(chat_id=7010118152, text="til bot_stwsasart da xatolik yuz berdi.")
        user = None
    finally:
        await db_user.disconnect()

    if user is None:
        await message.answer(f"Assalomu Alaykum!\nSiz ro'yxatdan o'tishingiz kerak")
        await message.answer(f"Ismingizni kiriting  : ", reply_markup=ReplyKeyboardRemove())
        await Qabul_State.ism.set()
    else:
        await message.answer(f"Assalomu Alaykum! ", reply_markup=bosh_menu)


@dp.message_handler(text="🇷🇺Русский")
async def bot_start_ru(message: types.Message):
    user_id = (str(message.from_user.id))
    try:
        await db_user.create()
    except:
        pas = 1

    try:
        user = await db_user.select_user(user_id=user_id)
    except:
        await bot.send_message(chat_id=7010118152, text="til bot_start_ru da xatolik yuz berdi.")
        user = None
    finally:
        await db_user.disconnect()

    if user is None:
        await message.answer(f"Здравствуйте!\nВы должны зарегистрироваться")
        await message.answer(f"Введите ваше имя  : ", reply_markup=ReplyKeyboardRemove())
        await Qabul_State_ru.ism.set()
    else:
        await message.answer(f"Здравствуйте!", reply_markup=bosh_menu_ru)
