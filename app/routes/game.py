from fastapi import APIRouter, HTTPException
from ..utils.generate_words import gets_words

game = APIRouter()

@game.get('/getWord/{word}')
async def get_word(word: str):
    data = await gets_words(word = word)
    return {"valideWords": data[0], "letters": data[1]}

@game.put('/putWord/{word}')
def put_word(word: str):
     pass