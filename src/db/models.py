from sqlalchemy import Column, Integer, String

from src.db import Base


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
