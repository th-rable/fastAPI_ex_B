from fastapi import APIRouter, Query, HTTPException
from typing import List, Union
from pydantic import BaseModel
from internal import UserStorage

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

class LoginItem(BaseModel):
    id: str
    psword: str

class RigisterItem(BaseModel):
    id: str
    psword: str
    name: str

@router.post("/login/")
async def login(item: LoginItem):
    result = UserStorage.Login(item)
    if not result['status']:
        raise HTTPException(status_code=404, detail=result['message'])
    return result['message']

@router.post("/register/")
async def register(item: RigisterItem):
    result = UserStorage.Register(item)
    if not result['status']:
        raise HTTPException(status_code=404, detail=result['message'])
    return result['message']