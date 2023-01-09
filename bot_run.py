from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    print('Бот вышел в онлайн!!!!')

from handler import client, admin, other
client.register_message_client(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
