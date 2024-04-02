#FASTAPI ( PATH PARAMETERS)

#BASIC PROGRAMS
#PATH PARAMETER AND QUERY PARAMETER

'''
from fastapi import FastAPI,Query

app=FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id:int, q: str=Query(None,min_len=3)):
    return{"item_id":item_id,"q":q}

'''

from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

items_db = []

app = FastAPI()

class Item(BaseModel):
    item_id: int
    name: str
    des: str = None
    price: float

@app.get("/items", response_model=List[Item])
def read_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    return items_db[item_id]

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    items_db[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    del items_db[item_id]
    return {"message": "Item deleted successfully"}



