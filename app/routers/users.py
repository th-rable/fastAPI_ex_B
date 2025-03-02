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

class RegisterItem(BaseModel):
    id: str
    psword: str
    name: str
    grade: int

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
async def register(item: RegisterItem):
    result = UserStorage.Register(item)
    if not result['ok']:
        return result
    logitem = LoginItem(id=item.id,psword=item.psword)
    result2 = await login(logitem)
    return result2

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

@router.post("/getname/")
async def getname(item: CheckIdItem):
    result = UserStorage.Getname(item)
    return result

@router.post("/logout/")
async def logout(item: CheckLoginItem):
    result = UserStorage.Logout(item)
    return result

