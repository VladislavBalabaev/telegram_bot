from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_load = KeyboardButton('Ensure upload')
button_delete = KeyboardButton('Cancel upload')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True,
                                        one_time_keyboard=True)