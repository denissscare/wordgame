import asyncio
import itertools
from typing import Any, Awaitable

import aiohttp
# from . import config

URL = f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20241023T115255Z.2dabe9097d8752fb.2dddff22b6bf055a3e4dfe504dc9239ea9c4d36d&lang=ru-ru&text='


def generate_words(word:str) -> tuple[set, set]:
    all_permutations = []
    letters = []

    for el in itertools.permutations(word,1):
        letters.append(''.join(el))

    for i in range(1, len(word)):
        for el in itertools.permutations(word,i+1):
            all_permutations.append(''.join(el))
    return set(all_permutations), set(letters)
   

async def dict_handler(array: set) -> list | dict:
    async with aiohttp.ClientSession() as session:
        tasks = []
        check = session.get(URL)
        print(await check)
        for word in array:
            tasks.append(asyncio.create_task(session.get(URL + word)))
        responses = await asyncio.gather(*tasks)
        data = [await r.json() for r in responses]

        if data[0]['code'] == 403:
            return data[0]
        return data


def get_valide_word(arr: list) -> list:
    result = []
    for el in arr:
        if(el['def']):
            result.append(el['def'][0]['text'])
    return result

async def gets_words(word: str) -> tuple:
    array_of_words = generate_words(word=word)
    words = await dict_handler(array_of_words[0])
    
    if not isinstance(words, list):
        return (words['code'], words['message'])

    letters = array_of_words[1]
    valide_word = get_valide_word(words)
    return (valide_word, letters)


if __name__ == '__main__':

    arr = generate_words('хлеб')
    words = asyncio.run(dict_handler(arr[0]))
    # print(get_valide_word(words))