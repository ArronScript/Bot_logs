import asyncio

from bot import dp, bot

from models import User
from models import Orders

from utils import db

db.create_tables()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
