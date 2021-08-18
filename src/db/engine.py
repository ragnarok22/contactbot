from src.db import Base, engine


def start_db():
    Base.metadata.create_all(engine)
