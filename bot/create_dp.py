from aiogram import Dispatcher
from .handlers import message_handler, callback_handler

dp = Dispatcher()
dp.include_router(callback_handler)
dp.include_router(message_handler)
