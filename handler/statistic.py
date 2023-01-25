# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import types, Dispatcher
# from keyboards.client_keyboards import choise_1, choise_stat
# from create_bot import bot
#
#
# class FSMAdmin_stat(StatesGroup):
#     id = State()
#     category_exp = State()
#     date_exp = State()
#
#
# async def statistics(callback_query: types.CallbackQuery):
#     # Получаем статитстику
#     await bot.send_message(callback_query.from_user.id, "Выбери какую статистику посмотреть", reply_markup=choise_stat)
#
#
# async def one_statistics(callback_query: types.CallbackQuery, state: FSMContext):
#     await FSMAdmin_stat.id.set()
#     async with state.proxy() as data:
#         data['id'] = callback_query.from_user.id
#     await FSMAdmin_stat.next()
#     await bot.send_message(callback_query.from_user.id, "Выбери категорию трат", reply_markup=choise_1)
#
#
# async def one_statistics_finish(callback_query: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_name'] = callback_query.from_user.first_name
#         data['category'] = callback_query.data
#     print(data)
#     await bot.send_message(callback_query.from_user.id, str(data))
#     await state.finish()
#
#
# async def all_statistics(callback_query: types.CallbackQuery):
#     data = [callback_query.from_user.id]
#     await bot.send_message(callback_query.from_user.id, str(data))
#
#
#
# def register_message_statistic(dp: Dispatcher):
#     dp.register_callback_query_handler(statistics, text="statistics")
#     dp.register_callback_query_handler(one_statistics, text='statistics_one', state=None)
#     dp.register_callback_query_handler(one_statistics_finish, state=FSMAdmin_stat.category_exp)
#     dp.register_message_handler(all_statistics, text='statistics_all')
