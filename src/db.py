from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import CLEARDB_DATABASE_URL

engine = create_engine(CLEARDB_DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# models


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)

    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __repr__(self):
        return f'Client ({self.first_name} {self.last_name})'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# engine
def start_db():
    Base.metadata.create_all(engine)
