from sqlalchemy import create_engine
from ..models.words import Base
import os

DB = 'sqlite:///' + os.path.abspath(os.getcwd())+"\words.db"


engine = create_engine(DB, echo=True)

def create_db_and_tables() -> None:
	Base.metadata.create_all(engine)
 
 
if __name__ == '__main__':
    create_db_and_tables()