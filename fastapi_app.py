from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

tasks = []

class Task(BaseModel):
    title: str
    description: str
    status: str = "In-progress"

# Create a task
@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task added successfully"}

# Get all tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Update a task (only the status is required)
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id >= len(tasks):
        return {"message": "Task ID not found"}
    
    # Update only the status field, keeping title and description intact
    tasks[task_id].status = task.status
    
    return {"message": "Task updated successfully"}

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id >= len(tasks):
        return {"message": "Task ID not found"}
    tasks.pop(task_id)
    return {"message": "Task deleted successfully"}
