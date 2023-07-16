from aiogram.utils import executor
from create_bot import dp
from database import db

async def on_startup(_):
    print('Bot started working')
    db.sql_start()

async def on_shutdown(_):
    print('Bot has finished working')


from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
# other.register_handler_other(dp)


executor.start_polling(dp,
                       skip_updates=True,
                       on_startup=on_startup,
                       on_shutdown=on_shutdown
                       )
# skip_updates=True for skipping updates when Bot is offline
