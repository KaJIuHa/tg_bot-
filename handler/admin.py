from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from keyboards.client_keyboards import choise_1, choise_2
from create_bot import bot


class FSMAdmin(StatesGroup):
    date = State()
    category = State()
    exp = State()
    id = State()


#     Запуск машины состояния, загрузка расходов в БД(пока внутренняя БД aiogram)
#  @dp.message_handler(commands='Добавить', state=None)
async def fsm_start(message: types.Message):
    await FSMAdmin.date.set()
    await bot.send_message(message.from_user.id, 'Добавить дату в формате дд.мм.год')


# Ловим первое сообщение в БД
# @dp.messega_handler(content_types=['date'], state=FSMAdmin.date)
async def load_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.from_user.id, 'Теперь выбери категорию трат', reply_markup=choise_1)


#  Ловим второе сообщение в БД
# @dp.messega_handler(content_types=['category'], state=FSMAdmin.category)
async def load_category(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = callback_query.data
    print(data)
    await FSMAdmin.next()
    await bot.send_message(callback_query.from_user.id, 'Теперь введи сумму')


#     Ловим третье сообщение в БД
# @dp.messega_handler(content_types=['expanses'], state=FSMAdmin.exp)
async def load_expanses(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['expanses'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.from_user.id, 'Теперь напиши "Ок" чтобы подтвердить ввод!\n'
                                                 'Если хочешь отменить ввод напиши "Отмена"', reply_markup=choise_2)


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


def register_message_admin(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands='Добавить', state=None)
    dp.register_message_handler(load_date, state=FSMAdmin.date)
    dp.register_callback_query_handler(load_category, state=FSMAdmin.category)
    dp.register_message_handler(load_expanses, state=FSMAdmin.exp)
    dp.register_callback_query_handler(load_id, state=FSMAdmin.id)
