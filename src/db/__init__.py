from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.settings import CLEARDB_DATABASE_URL

engine = create_engine(CLEARDB_DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
