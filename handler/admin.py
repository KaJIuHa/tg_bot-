from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from keyboards.client_keyboards import choise_1, choise_2, choise_inc
from create_bot import bot


# import google_sheet
# import string


class FSMAdmin(StatesGroup):
    date = State()
    category = State()
    exp = State()
    id = State()


class FSMAdmin_inc(StatesGroup):
    date = State()
    category = State()
    exp = State()
    id = State()


#     Запуск машины состояния, загрузка расходов в БД(пока внутренняя БД aiogram)
#  @dp.message_handler(commands='Добавить', state=None)
async def fsm_start(callback_query: types.CallbackQuery):
    await FSMAdmin.date.set()
    await bot.send_message(callback_query.from_user.id, '⏱️Добавить дату в формате дд.мм.гггг')


# Ловим первое сообщение в БД
# @dp.messega_handler(content_types=['date'], state=FSMAdmin.date)
async def load_date(message: types.Message, state: FSMContext):
    if message.text[2] == "." and message.text[5] == ".":
        if message.text.replace(".", "").isdigit():
            if int(message.text.replace(".", "")[0:2]) < 32 and int(message.text.replace(".", "")[2:4]) < 13:
                if int(message.text.replace(".", "")[4:6]) == 20:
                    async with state.proxy() as data:
                        data['date'] = message.text
                    await FSMAdmin.next()
                    await bot.send_message(message.from_user.id, 'Теперь выбери категорию траты', reply_markup=choise_1)
                else:
                    await bot.send_message(message.from_user.id, "💀Введена неверная дата, Введи снова")
            else:
                await bot.send_message(message.from_user.id, "💀Введена неверная дата, Введи снова")
        else:
            await bot.send_message(message.from_user.id, "💀Введена неверная дата, Введи снова")
    else:
        await bot.send_message(message.from_user.id, "💀Введена неверная дата, Введи снова")


#  Ловим второе сообщение в БД
# @dp.messega_handler(content_types=['category'], state=FSMAdmin.category)
async def load_category(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = callback_query.data
    print(data)
    await FSMAdmin.next()
    await bot.send_message(callback_query.from_user.id, '💸Теперь введи сумму')


#     Ловим третье сообщение в БД
# @dp.messega_handler(content_types=['expanses'], state=FSMAdmin.exp)
async def load_expanses(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['expanses'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, "Жми 👌 Подтвердить чтобы запсиать \n"
                                                     "или ⛔ Отмена чтобы я никогда не узнал что ты транжира",
                               reply_markup=choise_2)
    else:
        await bot.send_message(message.from_user.id, "💀Введена неверная сумма, Введи снова")


# Ловим четвертое собщение в БД
# @dp.messega_handler(content_types=['id'], state=FSMAdmin.exp)
async def load_id(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == "Yes":
        async with state.proxy() as data:
            data['id'] = callback_query.from_user.id
            data['name'] = callback_query.from_user.first_name
        await bot.send_message(callback_query.from_user.id, str(data))
        await state.finish()
    elif callback_query.data == "No":
        await bot.send_message(callback_query.from_user.id, "Отменил")
        await state.finish()


async def fsm_income_start(callback_query: types.CallbackQuery):
    await FSMAdmin_inc.date.set()
    await bot.send_message(callback_query.from_user.id, '⏱️Добавить дату в формате дд.мм.гггг')


async def load_income(message: types.Message, state: FSMContext):
    if message.text[2] == "." and message.text[5] == ".":
        if message.text.replace(".", "").isdigit():
            if int(message.text.replace(".", "")[0:2]) < 32 and int(message.text.replace(".", "")[2:4]) < 13:
                if int(message.text.replace(".", "")[4:6]) == 20:
                    async with state.proxy() as data:
                        data['date'] = message.text
                    await FSMAdmin_inc.next()
                    await bot.send_message(message.from_user.id, 'Теперь выбери категорию траты',
                                           reply_markup=choise_inc)
                else:
                    await bot.send_message(message.from_user.id, "💀Введена неверная дата, Введи снова")
            else:
                await bot.send_message(message.from_user.id, "💀Введена неверная дата, Введи снова")
        else:
            await bot.send_message(message.from_user.id, "💀Введена неверная дата, Введи снова")
    else:
        await bot.send_message(message.from_user.id, "💀Введена неверная дата, Введи снова")


async def inc_category(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = callback_query.data
    print(data)
    await FSMAdmin_inc.next()
    await bot.send_message(callback_query.from_user.id, '💸Теперь введи сумму')


async def inc_value(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['expanses'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, "Жми 👌 Подтвердить чтобы запсиать \n"
                                                     "или ⛔ Отмена чтобы я никогда не узнал что ты транжира",
                               reply_markup=choise_2)
    else:
        await bot.send_message(message.from_user.id, "💀Введена неверная сумма, Введи снова")


async def load_inc_id(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == "Yes":
        async with state.proxy() as data:
            data['id'] = callback_query.from_user.id
            data['name'] = callback_query.from_user.first_name
        await bot.send_message(callback_query.from_user.id, str(data))
        await state.finish()
    elif callback_query.data == "No":
        await bot.send_message(callback_query.from_user.id, "Отменил")
        await state.finish()


def register_message_admin(dp: Dispatcher):
    dp.register_callback_query_handler(fsm_start, text='add_expansis', state=None)
    dp.register_message_handler(load_date, state=FSMAdmin.date)
    dp.register_callback_query_handler(load_category, state=FSMAdmin.category)
    dp.register_message_handler(load_expanses, state=FSMAdmin.exp)
    dp.register_callback_query_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(fsm_income_start, text='add_income', state=None)
    dp.register_message_handler(load_income, state=FSMAdmin_inc.date)
    dp.register_callback_query_handler(inc_category, state=FSMAdmin_inc.category)
    dp.register_message_handler(inc_value, state=FSMAdmin_inc.exp)
    dp.register_callback_query_handler(load_inc_id, state=FSMAdmin_inc.id)
