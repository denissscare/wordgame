import os
from sqlalchemy import create_engine
from ..models.words import Base


DB = 'sqlite:///db/database.db'


engine = create_engine(DB, echo=True)

def create_db_and_tables() -> None:
	Base.metadata.create_all(engine)