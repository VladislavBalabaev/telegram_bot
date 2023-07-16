# Two types of TGbot:
# LongPolling - to test from local source, it checks updates while requesting for them
# Webhook - to deploy a bot, it gets updates from messages from(!) telegram

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = os.environ['TOKEN']

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


