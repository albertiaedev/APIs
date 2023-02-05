from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  description: str
  price: float
  tax: float=0.5

@app.get("/")
def read_root():
  return {"REST API CRUD built on FastAPI":"by J.A. Hernández"}

'''

The next code is for a REST API with basic CRUD operations.

Run this app using the command `uvicorn main:app --reload` and test it
using Postman or Curl as API client.

'''
# Create an item
@app.post("/item/")
async def create_item(item: Item):
  return item

# Read the item
@app.get("/item/{id}")
async def read_item(id: int, q: str=None):
  return {"id": id, "q": q}

# Update an item
@app.put("/item/{id}")
async def update_item(id: int, item: Item):
  return {"id": id, "item": item}

# Delete an item
@app.delete("/item/{id}")
asyn def delete_item(id: int):
  return {"id": id}
