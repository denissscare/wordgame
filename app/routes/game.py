from fastapi import APIRouter
from ..utils.generate_words import gets_words

game = APIRouter()

@game.get('/getWord/{word}')
async def getWord(word: str):
    data = await gets_words(word=word)
    return {"valideWords": data[0], "letters": data[1]}

