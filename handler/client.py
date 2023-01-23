from aiogram import types, Dispatcher
from keyboards.client_keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer("Привет!!!! Это наш личный бот для учета финансов.\n"
                         "Чтобы добавить что-то, нужно записать в виде собщения", reply_markup=kb_client)



def register_message_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
