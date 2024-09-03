from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from handlers.users.functions import checkinvoice
from keyboards.default.admin import admin_invoice, admin_only
from loader import dp


class InvoiceState(StatesGroup):
    invoice = State()


@dp.message_handler(text="Bosh sahifa Admin", state=InvoiceState.invoice)
async def admin_main(message: types.Message, state: FSMContext):
    await message.answer(f"Admin sahifaga hush kelibsiz", reply_markup=admin_invoice)
    await state.finish()


@dp.message_handler(text="/admin")
async def admin_main(message: types.Message):
    await message.answer(f"Admin sahifaga hush kelibsiz", reply_markup=admin_invoice)


@dp.message_handler(text="Invoice tekshirish")
async def admin_main1(message: types.Message):
    await message.answer(f"To'lov invoice raqamini kiriting", reply_markup=admin_only)
    await InvoiceState.invoice.set()


@dp.message_handler(lambda message: not message.text.isdigit(), state=InvoiceState.invoice)
async def admin3(message: types.Message):
    await message.answer(f"Iltimos bu yerga faqat raqam kiriting\n"
                         f"Masalan: 157901286")


@dp.message_handler(lambda message: message.text.isdigit(), state=InvoiceState.invoice)
async def admin4(message: types.Message):
    nomer = int(message.text)
    javob = ''
    javob += checkinvoice(nomer)
    print(javob)

    if javob == '':
        await message.answer(f"Ma'lumot mavjud emas.")
    else:
        await message.answer(f"{javob}")

