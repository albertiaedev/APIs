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

# Create an item
@app.post("/item/")
async def create_item(item: Item):
  return item

# Read the item
@app.get("/item/{id}")
async def read_item(id: int, q: str=None):
  return {"id": id, "q": q}
