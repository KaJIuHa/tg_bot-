from aiogram import types, Dispatcher
from keyboards.client_keyboards import choise_add


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer("Привет!!!! Это наш личный бот для учета финансов.\n"
                         "Он умеет записывать расходы или доходы\n"
                         "или выдавать статистику про расходы за период\n"
                         "Выбери что быдум делать", reply_markup=choise_add)

#

def register_message_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
