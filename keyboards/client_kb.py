from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Check')
b2 = KeyboardButton('Menu')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True,
                                one_time_keyboard=True)

kb_client.add(b1).insert(b2).add(b1, b2).row(b1, b2)
# add
# insert
# row