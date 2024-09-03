
from aiogram import types

from keyboards.default.menu import bosh_menu
from keyboards.default.menu_ru import bosh_menu_ru
from loader import dp


@dp.message_handler(text="🏠Bosh menu")
async def bot_start(message: types.Message):
    await message.delete()
    await message.answer(f"Assalomu Alaykum! ", reply_markup=bosh_menu)


@dp.message_handler(text="🏠Главное меню")
async def bot_start(message: types.Message):
    await message.delete()
    await message.answer(f"Привет! ", reply_markup=bosh_menu_ru)



@dp.message_handler(text="🏢Biz haqimizda")
async def qabmlaumot(message: types.Message):
    await message.answer(
        f"2017 yildan boshlab 'Djeksonvill' kompaniyasi Toshkentning eng yaxshi restoranlarini o'zining"
        f" noyob mahsulotlari bilan quvontirib kelmoqda, eng betakror kolbasalarni yaratmoqda. "
        f"Biz har bir kolbasa turli mamlakatlarning sayohatlari, kashfiyotlari va kulinariya san'atiga "
        f"bo'lgan ishtiyoqi haqida hikoya qilishi uchun aromatlar va ta'mlarni diqqat bilan "
        f"tanlaymiz.\n\n "
        f"Bizning mahsulotlarimiz o'zining eng yuqori sifati va betakror ta'm palitrasi bilan nufuzli "
        f"restoranlarning menyusining ajralmas qismiga aylandi. 'Djeksonvill' kolbaskalari – bu haqiqiy"
        f" ta'm zavqi uchun kerak bo'lgan hamma narsa.")


@dp.message_handler(text="🏢 О нас")
async def qabmlaumot_ru(message: types.Message):
    await message.answer(
        f"С 2017 года компания 'Джексонвилл' радует лучшие рестораны Ташкента своей уникальной продукцией, создавая "
        f"самые неповторимые колбасы. Мы тщательно отбираем ароматы и вкусы, чтобы каждая колбаса рассказывала историю "
        f"путешествий, открытий и страсти кулинарного искусства различных стран мира.\n\n"
        f"Наша продукция стала неотъемлемой частью меню престижных ресторанов благодаря своему высочайшему "
        f"качеству и неповторимой вкусовой палитре. Колбаски 'Джексонвилл' – это все, что вам нужно для истинного"
        f" вкусового наслаждения.")
