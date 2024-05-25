from sqlalchemy import ForeignKey, String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import User
from utils.db_base import Base


class Orders(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    logs_types: Mapped[str] = mapped_column(String())
    status: Mapped[str] = mapped_column(String())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


    user: Mapped["User"] = relationship(back_populates="orderess")