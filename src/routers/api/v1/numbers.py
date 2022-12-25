from typing import List

from fastapi import APIRouter, Query, Depends

from src.models import User_Pydantic
from src.service.auth import get_current_user
from src.utils.get_value_remains import get_value_remains, generate_list

router_number = APIRouter(prefix="/numbers", tags=['numbers'])


@router_number.get("/", summary="Get remains value with list")
async def get(
        numbers: List[int] = Query(),
        user: User_Pydantic = Depends(get_current_user)
):
    """
    Get remains values with list

    - **numbers**: List integer values

    \f
    :param numbers: List integer values
    :param user:
    :return:
    """
    return {"information": (i for i in generate_list(numbers))}


@router_number.get("/{number}", summary="Get remains value")
async def get(
        number: int,
        user: User_Pydantic = Depends(get_current_user)
):
    """
    Get remains value

    - **number**: Value integer

    \f
    :param number: Value integer
    :param user:
    :return:
    """
    return {"information": get_value_remains(number)}
