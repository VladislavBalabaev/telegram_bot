from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from database import db
from handlers.admin import IDs

# @dp.message_handler(commands = ['start'])
async def command_start(message: types.Message):
    try:
        # await bot.send_message(message.from_user.id, 'Bon appétit')
        await bot.send_message(message.from_user.id, 'Bon appétit', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Something went wrong, sorry :(')


# @dp.message_handler() # if we capture message in one handler it won't go to other handlers
# async def echo_send(message: types.Message):
    # await message.answer('message.text')    # we can answer in group chat!
    # await message.reply('message.text')     # we can reply in group chat!
    # await bot.send_message(message.from_user.id, 'message.text')    # to text directly into chat with Bot;
    # pass

# @dp.message_handler(commands=['DF'])
async def show_df_command(message: types.Message):
    if message.from_user.id in IDs:
        try:
            await bot.send_message(message.from_user.id, f'Length of DF: {db.sql_read()}')
        except:
            await bot.send_message(message.from_user.id, "You're not a moderator, sorry :)")

# !!!
# @dp.message_handler(lambda message: 'taxi' in message.text)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(show_df_command, commands=['DF'])
