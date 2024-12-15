from fastapi import APIRouter, Query
from typing import List, Union
from pydantic import BaseModel
import sockets as sio
router = APIRouter(
    prefix="/socket",
    tags=["socket test"]
)

class Message(BaseModel):
    message: Union[str, None] = ""

@router.post("/")
async def sendMessage(item: Message):
    await sio.sio_server.send(item.message)
    return {"OK"}
@router.get("/")
async def getUserId():
    return sio.sidList