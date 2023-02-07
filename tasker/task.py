from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the model we´ll use for creating, reading, updating and deleting the tasks
class Tasks(BaseModel):
  task: str
  description: str


# Now we create a list to store tasks in memory
# Use a SQL/NoSQL database to store the data when you deploy the app to production
tasks = []
