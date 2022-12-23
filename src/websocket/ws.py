from typing import Union

from fastapi import (
    Depends,
    WebSocket,
    APIRouter,
)

from src.service.ws import get_cookie_or_token
from src.utils.get_value_remains import get_value_remains

router_ws = APIRouter()


@router_ws.websocket("/items/{item_id}/ws")
async def websocket_endpoint(
        websocket: WebSocket,
        item_id: str,
        q: Union[int, None] = None,
        cookie_or_token: str = Depends(get_cookie_or_token),
):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()

        if q is not None:
            await websocket.send_text(f"Query parameter q is: {q}")
            return

        try:
            val = int(data)
            value_remains = get_value_remains(val)
            if len(value_remains) != 0:
                await websocket.send_text(f"{value_remains}")
            else:
                await websocket.send_text(f"Value not remains")
        except:
            await websocket.send_text(f"Error - Please value integer")
