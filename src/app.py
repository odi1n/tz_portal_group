from typing import List

from fastapi import FastAPI, Query

from src.utils.get_value_remains import get_value_remains, generate_list

app = FastAPI()


@app.get("/numbers/")
async def get(numbers: List[int] = Query(None)):
    value_remains = (i for i in generate_list(numbers))
    return {"information": value_remains}


@app.get("/numbers/{number}")
async def get(number: int):
    return {"information": get_value_remains(number)}
