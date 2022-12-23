from typing import List

from fastapi import APIRouter, Query

from src.utils.get_value_remains import get_value_remains, generate_list

router_number = APIRouter(prefix="/numbers", tags=['numbers'])


@router_number.get("/")
async def get(numbers: List[int] = Query()):
    value_remains = (i for i in generate_list(numbers))
    return {"information": value_remains}


@router_number.get("/{number}")
async def get(number: int):
    return {"information": get_value_remains(number)}
