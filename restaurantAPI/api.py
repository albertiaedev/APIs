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