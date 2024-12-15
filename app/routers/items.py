from fastapi import APIRouter, Query
from typing import List, Union
from pydantic import BaseModel

router = APIRouter(
    prefix="",
    tags=["items"]
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class Item2(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@router.post("/items/")
async def create_item(item: Item):
    return item

@router.get("/items1/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=5, pattern="^1")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items_list/")
async def read_items(q: Union[List[str], None] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items