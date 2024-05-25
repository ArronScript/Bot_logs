from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

from bot.settings import settings
from models import User
from data.choice_list import change_name


class WorkChoice(CallbackData, prefix="work"):
    callback: str


class EditOrd(CallbackData, prefix="status"):
    callback: str
    order_id: str


work = InlineKeyboardButton(text="🗂Отправить на отработку", callback_data="work")

profile = InlineKeyboardButton(text="👤Профиль", callback_data="profile")
conn = InlineKeyboardButton(text="📞Связь", callback_data="conn")

rules = InlineKeyboardButton(text="📄Правила", callback_data="rules")

current_requests = InlineKeyboardButton(
    text="💸Актуальные запросы", callback_data="current_requests"
)

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[work], [profile, conn], [rules], [current_requests]]
)


# Подтвердить Отмена


def create_work_choice(choice_keys_list=None) -> InlineKeyboardMarkup:
    steam_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["steam"],
        callback_data=WorkChoice(callback="steam").pack(),
    )
    epic_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["epic"],
        callback_data=WorkChoice(callback="epic").pack(),
    )
    riot_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["riot"],
        callback_data=WorkChoice(callback="riot").pack(),
    )
    roblox_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["roblox"],
        callback_data=WorkChoice(callback="roblox").pack(),
    )
    ea_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["ea"],
        callback_data=WorkChoice(callback="ea").pack(),
    )
    battlenet_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["battlenet"],
        callback_data=WorkChoice(callback="battlenet").pack(),
    )
    supercell_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["supercell"],
        callback_data=WorkChoice(callback="supercell").pack(),
    )
    tarkov_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["tarkov"],
        callback_data=WorkChoice(callback="tarkov").pack(),
    )
    ubisoft_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["ubisoft"],
        callback_data=WorkChoice(callback="ubisoft").pack(),
    )
    rockstar_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["rockstar"],
        callback_data=WorkChoice(callback="rockstar").pack(),
    )
    mihoyo_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["mihoyo"],
        callback_data=WorkChoice(callback="mihoyo").pack(),
    )
    minecraft_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["minecraft"],
        callback_data=WorkChoice(callback="minecraft").pack(),
    )
    pubg_mobile_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["pubg_mobile"],
        callback_data=WorkChoice(callback="pubg_mobile").pack(),
    )
    albion_button = InlineKeyboardButton(
        text=change_name(choice_keys_list)["albion"],
        callback_data=WorkChoice(callback="albion").pack(),
    )
    current_button = InlineKeyboardButton(
        text="Подтвердить", callback_data="current_work"
    )
    back_menu_button = InlineKeyboardButton(text="Назад", callback_data="back_menu")

    work_choice_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [steam_button, epic_button],
            [riot_button, roblox_button],
            [ea_button, battlenet_button],
            [supercell_button, tarkov_button],
            [ubisoft_button, rockstar_button],
            [mihoyo_button, minecraft_button],
            [pubg_mobile_button, albion_button],
            [current_button, back_menu_button],
        ]
    )
    return work_choice_keyboard


def back_menu() -> InlineKeyboardMarkup:
    back_menu_button = InlineKeyboardButton(
        text="Назад", callback_data="back_menu_solo"
    )
    back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[back_menu_button]])
    return back_keyboard


def back_menu_profile() -> InlineKeyboardMarkup:
    back_menu_button = InlineKeyboardButton(
        text="Назад", callback_data="back_menu_solo_profile"
    )
    orders_list_button = InlineKeyboardButton(text="Заявки", callback_data="my_orders")
    back_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[orders_list_button], [back_menu_button]]
    )
    return back_keyboard


def back_menu_orders() -> InlineKeyboardMarkup:
    back_menu_button = InlineKeyboardButton(
        text="Назад", callback_data="back_menu_solo_profile"
    )
    back_keyboard = InlineKeyboardMarkup(inline_keyboard=[[back_menu_button]])
    return back_keyboard


def call_kb() -> InlineKeyboardMarkup:
    helper_button = InlineKeyboardButton(text="Поддержка", url=settings.url_helper)
    forum_button = InlineKeyboardButton(text="Поддержка", url=settings.url_forum)

    back_menu_button = InlineKeyboardButton(
        text="Назад", callback_data="back_menu_solo_profile"
    )
    call_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[helper_button], [forum_button], [back_menu_button]]
    )
    return call_keyboard


def edit_status_order_kb(order_id):
    hire_button = InlineKeyboardButton(text="Принять в работу",
                                       callback_data=EditOrd(callback='heir', order_id=order_id).pack())
    reject_button = InlineKeyboardButton(text="Отклонить",
                                         callback_data=EditOrd(callback="reject", order_id=order_id).pack())
    pay_button = InlineKeyboardButton(text="Выплачена", callback_data=EditOrd(callback="pay", order_id=order_id).pack())
    edit_status_order = InlineKeyboardMarkup(
        inline_keyboard=[[hire_button], [reject_button], [pay_button]]
    )
    return edit_status_order
