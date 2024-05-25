import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = sqlalchemy.create_engine('sqlite:///data/db.db')
Session = sessionmaker(bind=engine)
session = Session()
