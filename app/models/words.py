from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy import String, Column, Integer, ARRAY

class Base(DeclarativeBase):
    pass

class WordsBase(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String)
    sub_words:Column = Column(ARRAY(String, dimensions=1))
    
