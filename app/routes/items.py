from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Item(BaseModel):
    id: int
    name: str

# In real app this comes from DB
FAKE_DB = [
    Item(id=1, name="Item One"),
    Item(id=2, name="Item Two"),
    Item(id=3, name="Item Three"),
]

@router.get("/items", response_model=List[Item])
async def get_items():
    return FAKE_DB