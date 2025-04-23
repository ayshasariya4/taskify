from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# List to store tasks
tasks = []

class Task(BaseModel):
    title: str
    description: str
    status: str = "In-progress"

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task added successfully"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.put("/tasks/{task_id}")
def update_task(task_id: int, status: str):
    if status not in ["In-progress", "Completed"]:
        return {"message": "Invalid status"}
    tasks[task_id].status = status
    return {"message": "Task updated successfully"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks.pop(task_id)
    return {"message": "Task deleted successfully"}
