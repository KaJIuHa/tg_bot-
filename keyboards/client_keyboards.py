from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # ,ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

hi = KeyboardButton('/Привет')
start = KeyboardButton('/start')
help = KeyboardButton('/help')

in_avto = InlineKeyboardButton("🏎️ Машина", callback_data="avto")
in_gas = InlineKeyboardButton("⛽ Заправка", callback_data="gas")
in_credit = InlineKeyboardButton("💳 Кредит", callback_data="credit")
in_komunal = InlineKeyboardButton("💡 Комуналка", callback_data="comunal")
in_health = InlineKeyboardButton("🏥 Здоровье", callback_data="health")
in_sport = InlineKeyboardButton("🏅 Спорт", callback_data="sport")
in_food = InlineKeyboardButton("🥑 Еда", callback_data="food")
in_fastfood = InlineKeyboardButton("🥡 Фастфуд/Ресторан", callback_data="fastfood")
in_home = InlineKeyboardButton("🏠 Товары для дома", callback_data="home")
in_to_my = InlineKeyboardButton("💃 Одежда", callback_data='dress')
in_study = InlineKeyboardButton("🎓 Учеба/Расходники", callback_data='study')
in_some = InlineKeyboardButton("❓ Непредвиденные расходы", callback_data="some")
in_private = InlineKeyboardButton("🔒 Личные расходы", callback_data='private')
choise_1 = InlineKeyboardMarkup(row_width=2).row(in_gas, in_avto).row(in_credit, in_komunal).row(in_some,
                                                                                                 in_fastfood).row(
    in_home, in_study).row(in_health, in_to_my).row(in_food, in_private, in_sport)

in_kb_in1 = InlineKeyboardButton('💰 Зарплата',callback_data='salary')
in_kb_in2 = InlineKeyboardButton("👛 Аванс", callback_data='prepaid')
in_kb_in3 = InlineKeyboardButton('😎 Другое', callback_data='other')
choise_inc = InlineKeyboardMarkup().row(in_kb_in1,in_kb_in2,in_kb_in3)

in_kb_no = InlineKeyboardButton("⛔ Отмена", callback_data="No")
in_kb_yes = InlineKeyboardButton("👌 Подтвердить", callback_data="Yes")
choise_2 = InlineKeyboardMarkup(row_width=2).row(in_kb_yes, in_kb_no)

in_kb_add_exp = InlineKeyboardButton('📉 Добавить расход', callback_data='add_expansis')
in_kb_add = InlineKeyboardButton('📈 Добавить поступление', callback_data='add_income')
in_kb_stat = InlineKeyboardButton('🧮 Статитстика', callback_data='statistics')
choise_add = InlineKeyboardMarkup().row(in_kb_add,in_kb_add_exp).add(in_kb_stat)

in_kb_stat_one = InlineKeyboardButton("📉 Расходы по одной категрии", callback_data='statistics_one')
in_kb_stat_all = InlineKeyboardButton('📊 Расходы по всем категориям', callback_data='statistics_all')
in_kb_stat_inc = InlineKeyboardButton("💰 Доходы", callback_data='statistics_income')
choise_stat = InlineKeyboardMarkup(row_width=2).add(in_kb_stat_one).add(in_kb_stat_all).add(in_kb_stat_inc)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(hi).row(start, help).row(help)
