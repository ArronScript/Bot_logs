import json

from aiogram import Router, types, F
from aiogram.enums import ChatMemberStatus
from aiogram.fsm.context import FSMContext
from aiogram.methods.get_file import GetFile


from bot.keyboards import create_work_choice, WorkChoice, start_keyboard, back_menu, back_menu_profile, back_menu_orders, call_kb, EditOrd
from bot.state import UserState
from bot.create_bot import bot

from data.choice_list import change_name

from models import User, Orders
from utils import session

callback_handler = Router()

choice_list: dict[str, list[str]] = {}

# отраб


@callback_handler.callback_query(F.data == "work")
async def choose_work(query: types.CallbackQuery, state: FSMContext) -> None:
    await query.message.edit_text(
        text="Выберете что будете отрабатывать", reply_markup=create_work_choice()
    )

    choice_list.update({str(query.from_user.id): []})

    await state.set_state(UserState.choice_work)


# назад в меню
@callback_handler.callback_query(F.data == "back_menu_solo")
@callback_handler.callback_query(F.data == "back_menu")
async def choose_work(query: types.CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    choice_list[str(query.from_user.id)].clear()

    await query.message.edit_text(
        text=f"👋Приветствую, {query.from_user.first_name}\n"
        f"\n"
        f"📂Это телеграм бот для автоматического принятия файлов с вашими запросами!",
        reply_markup=start_keyboard,
    )

@callback_handler.callback_query(F.data == "back_menu_solo_profile")
async def choose_work_notclearstate(query: types.CallbackQuery) -> None:

    await query.message.edit_text(
        text=f"👋Приветствую, {query.from_user.first_name}\n"
        f"\n"
        f"📂Это телеграм бот для автоматического принятия файлов с вашими запросами!",
        reply_markup=start_keyboard,
    )



@callback_handler.callback_query(UserState.choice_work, WorkChoice.filter())
async def choose_work_selection(
    query: types.CallbackQuery, callback_data: WorkChoice
) -> None:
    if callback_data.callback in choice_list[str(query.from_user.id)]:
        choice_list[str(query.from_user.id)].remove(callback_data.callback)
    else:
        choice_list[str(query.from_user.id)].append(callback_data.callback)

    change_name(choice_keys=choice_list[str(query.from_user.id)])

    await query.message.edit_text(
        text="Выберете что будете отрабатывать",
        reply_markup=create_work_choice(
            choice_keys_list=choice_list[str(query.from_user.id)]
        ),
    )


@callback_handler.callback_query(F.data == "current_work")
async def not_select_category(query: types.CallbackQuery, state: FSMContext) -> None:
    if not choice_list[str(query.from_user.id)]:
        await query.message.edit_text(
            text="Вы не выбрали категорию!",
            reply_markup=back_menu(),
        )

    else:
        await state.set_state(UserState.wait_file)
        await state.set_data(choice_list)
        await query.message.edit_text(
            text=f"Отлично!\n"
                 f"Теперь отпрвате файл с логами:",
            reply_markup=back_menu(),
        )

@callback_handler.callback_query(F.data == 'profile')
async def profile(query: types.CallbackQuery, state: FSMContext) -> None:
    await query.message.edit_text(
        text=f"📔 Личный кабинет\n"
             f"\n"
             f"💎 Уникальный ID: {query.from_user.id}\n"
             f"👤Никнейм: {query.from_user.username}\n"
             f"💸Баланс: {session.query(User).filter(User.telegram_id == query.from_user.id).first().balance}\n"
             f"\n"
             f"💲 Вы заработали с нами: {session.query(User).filter(User.telegram_id == query.from_user.id).first().all_time_balance} рублей",

        reply_markup=back_menu_profile(),
    )

@callback_handler.callback_query(F.data == 'my_orders')
async def ord_list_profile(query: types.CallbackQuery) -> None:
    orders = session.query(Orders).filter(Orders.user_id == query.from_user.id)
    temp_id_stat = ''
    for i in orders:
        temp_id_stat += f'#{i.id} статус: {i.status}\n'

    await query.message.edit_text(
        text=f'Список заявок:\n'
             f'{temp_id_stat}',
        reply_markup=back_menu_orders()
    )

@callback_handler.callback_query(F.data == 'conn')
async def conn_links(query: types.CallbackQuery) -> None:
    await query.message.edit_text(
        text='Вот все актуальные ссылочки!',
        reply_markup=call_kb()
    )

@callback_handler.callback_query(F.data == 'rules')
async def profile(query: types.CallbackQuery) -> None:
    await query.message.edit_text(
        text='⚠️Процент отработки: 70/30%\n'
             '⚠️Для чека используем: Simple Checker, результаты отрабатываются руками.\n'
             '⚠️Не беру логи с облак (обсуждаемо) и раздач, СНГ логи.\n'
             '⚠️Беру от 5 логов, свежестью до 2х недель.',
        reply_markup=back_menu_orders()
    )

@callback_handler.callback_query(EditOrd.filter())
async def edit_status(query: types.CallbackQuery, callback_data: EditOrd) -> None:

    order = session.query(Orders).filter(Orders.id == callback_data.order_id).first()
    match callback_data.callback:
        case "heir":
            order.status = 'В работе'

        case "reject":
            order.status = 'Отклонена'

        case "pay":
            order.status = 'Выплачена'

    await bot.send_message(
        text=f'Статус заявки #{order.id} изменен!',
        chat_id=order.user_id
    )
    session.commit()


@callback_handler.callback_query(F.data == 'current_requests')
async def profile(query: types.CallbackQuery) -> None:
    await query.message.edit_text(
        text='Мы отрабатываем:\n'
             '<code>Steam</code>\n'
             '<code>Mihoyo</code>\n'
             '<code>EpicGames</code>\n'
             '<code>Battle.net</code>\n'
             '<code>Tarkov</code>\n'
             '<code>Minecraft</code>\n'
             '<code>RiotGames</code>\n'
             '<code>Roblox</code>\n'
             '<code>EA+Ubisoft</code>\n'
             '<code>Pubg mobile</code>\n'
             '<code>Supercell</code>\n'
             '<code>Rockstar games</code>\n'
             '<code>Albion</code>',
        reply_markup=back_menu_orders()
    )