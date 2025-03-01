from fastapi import APIRouter, Query, HTTPException
from typing import List, Union
from pydantic import BaseModel
from internal import UserStorage

router = APIRouter(
    prefix='/api/auth',
    tags=['Auth']
)

class LoginItem(BaseModel):
    id: str
    psword: str

class RigisterItem(BaseModel):
    id: str
    psword: str
    name: str
class CheckLoginItem(BaseModel):
    id: str
    key: str
class CheckIdItem(BaseModel):
    id: str

@router.post("/login/")
async def login(item: LoginItem):
    result = UserStorage.Login(item)
    if not result['status']:
        raise HTTPException(status_code=401, detail=result['message'])
    return result

@router.post("/register/")
async def register(item: RigisterItem):
    result = UserStorage.Register(item)
    if not result['status']:
        raise HTTPException(status_code=401, detail=result['message'])
    return result['message']

@router.post("/checklogin/")
async def checklogin(item: CheckLoginItem):
    result = UserStorage.CheckLogin(item)
    if not result['status']:
        raise HTTPException(status_code=401, detail=result['message'])
    return result

@router.post("/loginid_check/")
async def loginid_check(item: CheckIdItem):
    result = UserStorage.CheckId(item)
    return result