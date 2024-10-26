from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from utils.generate_words import gets_words
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/getWord/{word}')
async def getWord(word: str):
    data = await gets_words(word=word)
    return {"valideWords": data[0], "letters": data[1]}