from aiogram import Bot
from .settings import settings

bot = Bot(token=settings.token, parse_mode="html")
