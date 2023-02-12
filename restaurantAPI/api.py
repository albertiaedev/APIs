from fastapi import FastAPI
from pydantic import BaseModel

# Set the app

app = FastAPI()


# Create a class instance of the dishes in the menu

class Dish(BaseModel):
  name: str
  description: str
  price: float
  tax: float


#Create a dish in the menu 
@app.post("/menu")
async def create_menu(dish: Dish):
  return {"name": dish.name,
          "description": dish.description,
          "price": dish.price,
          "tax":dish.tax}

#Read a dish in the menu
@app.get("/menu/{id}")
async def read_menu(id: int, q: str=None):
  return {"id": id, "q": q}

#Update a dish in the menu
@app.put("/menu/{id}")
async def update_menu(id: int, dish: Dish):
  return {"id": id, "dish": dish}
