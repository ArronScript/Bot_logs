from .db import Database
from .db_base import session


db = Database(session=session)
