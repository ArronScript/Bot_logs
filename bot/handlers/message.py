from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.create_bot import bot
from bot.keyboards import start_keyboard, back_menu, edit_status_order_kb
from bot.settings import settings
from bot.state import UserState

from models import User, Orders
from utils import session

message_handler = Router()


@message_handler.message(CommandStart())
async def start(message: types.Message) -> None:
    user_main = session.query(User).filter(User.telegram_id == message.from_user.id).first()
    if not user_main:
        new_user = User(telegram_id=message.from_user.id, username=message.from_user.username, balance=0,
                        all_time_balance=0)
        session.add(new_user)
        session.commit()
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'👋Приветствую, {message.from_user.first_name}\n'
             f'\n'
             f'📂Это телеграм бот для автоматического принятия файлов с вашими запросами!',
        reply_markup=start_keyboard
    )


@message_handler.message(F.document, UserState.wait_file)
async def get_file(message: types.Message, state: FSMContext):
    if message.document.file_size > 24:
        tp_log = await state.get_data()
        order = Orders(logs_types=' '.join(tp_log[str(message.from_user.id)]),
                       status="Очередь", user_id=message.from_user.id)
        session.add(order)
        session.commit()

        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'Заявка успешно оставленна #{order.id}',
            reply_markup=back_menu()
        )

        await bot.send_document(
            document=message.document.file_id,
            chat_id=settings.admins[0],
        )

        await bot.send_message(
            text='Новый лог!\n'
                 f'ID заявки: {order.id}\n'
                 f'Логи: {order.logs_types}\n'
                 f'Статус: {order.status}\n'
                 f'ID логера: {order.user_id}\n'
                 f'Username логера: @{session.query(User).filter(User.telegram_id == order.user_id).first().username}',
            chat_id=settings.admins[0],
            reply_markup=edit_status_order_kb(order_id=str(order.id))
        )
    else:

        await bot.send_message(
            chat_id=message.from_user.id,
            text='Ваш файл пустой!',
            reply_markup=back_menu()

        )




