from sqlalchemy.orm import Session
from utils.db_base import Base, engine


class Database:
    def __init__(self, session: Session):
        self.session = session

    @staticmethod
    def create_tables() -> None:
        """
        creating all tables
        """
        Base.metadata.create_all(engine)

    def add(self, model: Base) -> None:
        """
        :param model: model to be added
        """
        self.session.add(model)
        self.session.commit()
