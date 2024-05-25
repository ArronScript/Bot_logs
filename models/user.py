from datetime import datetime
from typing import TYPE_CHECKING, Optional, List
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from utils.db_base import Base, session

if TYPE_CHECKING:
    from models import Orders


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[str] = mapped_column(String())
    username: Mapped[str] = mapped_column(String())
    balance: Mapped[str] = mapped_column(String())
    all_time_balance: Mapped[str] = mapped_column(String())

    orderess: Mapped[List["Orders"]] = relationship(
    back_populates = "user", cascade = "all, delete-orphan"
    )
    


