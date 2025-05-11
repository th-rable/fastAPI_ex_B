from fastapi import APIRouter, Query, HTTPException
from typing import List, Union
from pydantic import BaseModel
from internal import GlobalStorage
from internal import UserStorage

router = APIRouter(
    prefix='/api',
    tags=['api']
)
class CheckIdItem(BaseModel):
    id: str

@router.post("/getdday/")
async def getdday(item: CheckIdItem):
    if not UserStorage.CheckId(CheckIdItem).result :
        return {'result':False,'message':'id error'}

    grade = UserStorage.Getgrade(CheckIdItem)
    examlist = GlobalStorage.examlist
    returnlist = []
    for x in examlist:
        if x.grade != grade:
            continue
        


    return list2025
    

