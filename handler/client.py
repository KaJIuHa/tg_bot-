from aiogram import types, Dispatcher
from create_bot import dp, bot


# @dp.message_handler()
async def welcome_sendler(message: types.Message):
    if message.text == "Привет" and message.from_user.id == 1321338626:
        await message.answer("_____Привет хозяйка!!!!_____")
    elif message.text == "Привет" and message.from_user.id == 1578545286:
        await message.answer("____Привет создатель!!!!____")
    elif message.text == "Привет" and message.from_user.id == 5630610750:
        await message.answer('____ Опять работа___(((((')
    else:
        await message.answer("Ты кто такой??? Иди отсюда!!!!")


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer("Привет!!!! Это наш личный бот для учета финансов.\n"
                         "Чтобы добавить что-то, нужно записать в виде собщения")


def register_message_client(dp: Dispatcher):
    dp.register_message_handler(welcome_sendler)
    dp.register_message_handler(command_start, commands=['start', 'help'])
