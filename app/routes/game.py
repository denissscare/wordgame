from fastapi import APIRouter, HTTPException
from ..utils.generate_words import gets_words

game = APIRouter()

@game.get('/getWord/{word}')
async def getWord(word: str):
    data = await gets_words(word = word)
    
    if data[0] == 403:
        print('err')
        raise HTTPException(status_code = 403, detail = data[1])
    
    return {"valideWords": data[0], "letters": data[1]}

