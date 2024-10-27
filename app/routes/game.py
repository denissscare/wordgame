from fastapi import APIRouter, HTTPException
from ..utils.generate_words import gets_words
from ..db.db import engine
from sqlalchemy.orm import Session
from sqlalchemy import select 
from ..models.words import WordsBase



game = APIRouter()

@game.get('/getWord/{word}')
async def get_word(word: str):
    with Session(engine) as session:
        statement = select(WordsBase).where(WordsBase.word == word)
        if(statement):
            objects = session.scalars(statement).all()
            return object
        data = await gets_words(word = word)
        return {"valideWords": data[0], "letters": data[1]}

@game.put('/putWord/{word}')
def put_word(word: str):
     pass