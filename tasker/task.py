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

# Route to retrieve all the tasks
@app.get("/tasks")
async def read_task():
  return {"tasks": tasks}

# Route to create a new task
@app.post("/tasks")
async def create_task(task: Tasks):
  tasks.append(task.dict())
  return {"task": task}

# Route to update a task by its index in the list
@app.put("/task/{id}")
async def update_task(id: int, task: Tasks):
  tasks[id] = task.dict()
  return {"task": task}
