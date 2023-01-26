from aiogram.utils import executor
from create_bot import dp
from handler import client, admin, other, statistic
import logging


async def on_startup(_):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    print('Бот вышел в онлайн!!!!')


client.register_message_client(dp)
admin.register_message_admin(dp)
# statistic.register_message_statistic(dp)
other.register_message_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
