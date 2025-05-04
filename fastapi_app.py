from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from database import get_db, TaskModel

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    status: str = "In-progress"

class TaskOut(Task):
    id: int

@app.post("/tasks")
def create_task(task: Task, db: Session = Depends(get_db)):
    db_task = TaskModel(title=task.title, description=task.description, status=task.status)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {"message": "Task added successfully"}

@app.get("/tasks", response_model=List[TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(TaskModel).all()

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: Task, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = updated.title
    task.description = updated.description
    task.status = updated.status
    db.commit()
    return {"message": "Task updated successfully"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
