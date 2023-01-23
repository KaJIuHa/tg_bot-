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
choise_1 = InlineKeyboardMarkup(row_width=2).row(in_gas, in_avto, in_credit, in_komunal, in_food, in_fastfood, in_home,
                                                 in_study, in_health, in_to_my, in_some, in_private, in_sport)
in_kb_no = InlineKeyboardButton("⛔ Отмена", callback_data="No")
in_kb_yes = InlineKeyboardButton("👌 Подтвердить", callback_data="Yes")
choise_2 = InlineKeyboardMarkup(row_width=2).row(in_kb_yes, in_kb_no)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(hi).row(start, help).row(help)
