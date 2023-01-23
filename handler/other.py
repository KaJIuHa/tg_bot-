from aiogram import types, Dispatcher
from keyboards import kb_client


async def welcome_sendler(message: types.Message):
    if message.from_user.id == 1321338626:
        await message.answer("_____Привет хозяйка!!!!_____", reply_markup=kb_client)
    elif message.from_user.id == 1578545286:
        await message.answer("____Привет создатель!!!!____", reply_markup=kb_client)
    elif message.from_user.id == 5630610750:
        await message.answer('____ Опять работа___(((((', reply_markup=kb_client)
    else:
        await message.answer("Ты кто такой??? Иди отсюда!!!!")


def register_message_other(dp: Dispatcher):
    dp.register_message_handler(welcome_sendler, commands=["Привет"])
