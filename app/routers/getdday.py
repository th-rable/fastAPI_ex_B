from fastapi import APIRouter, Query, HTTPException
from typing import List, Union
from pydantic import BaseModel
from internal import GlobalStorage

router = APIRouter(
    prefix='/api',
    tags=['api']
)

@router.get("/getdday/")
async def getdday():
    list2025 = GlobalStorage.examList['2025']
    return list2025
    

