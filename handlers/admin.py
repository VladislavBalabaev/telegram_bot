from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot
from database import db
from keyboards import admin_kb

IDs = [749410326]

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

# Start of dialogue
# First question
# dp.message_handler(commands=['upload'], state=None)
async def cm_start(message: types.Message):
    global IDs
    if message.from_user.id in IDs:
        # await FSMAdmin.photo.set()
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id,
                               'HOW DO YOU LIKE IT?\n(To cancel parsing: "/cancel")',
                               reply_markup=admin_kb.button_case_admin)
    else:
        await bot.send_message(message.from_user.id, "You're not a moderator, sorry :)")

# @dp.message_handler(state='*', commands=['cancel'])
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    global IDs
    if message.from_user.id in IDs:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply("You've canceled setting.")

# First answer
# dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    global IDs
    if message.from_user.id in IDs:
        async with state.proxy() as data:
            data['param1'] = message.text
        # await FSMAdmin.next()
        # await message.reply('Give me a description')

        # async with state.proxy() as data:
        #     await message.answer(str(data))
        await bot.send_message(message.from_user.id, "Settings are set! Trying to start parsing!")
        # await db.sql_add_commit(state) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        await state.finish()

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['start_parsing'], state=None)
    dp.register_message_handler(cancel_handler, commands=['cancel'], state='*')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
