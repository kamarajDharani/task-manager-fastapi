from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..dependencies import get_db

router = APIRouter()


# CREATE TASK
@router.post("/tasks")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):

    new_task = models.Task(
        title=task.title,
        completed=False
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# GET TASKS
@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):

    tasks = db.query(models.Task).all()

    return tasks


# COMPLETE TASK
@router.put("/tasks/{task_id}")
def complete_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    task.completed = True

    db.commit()

    return {"message": "Task completed"}


# DELETE TASK
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    db.delete(task)

    db.commit()

    return {"message": "Task deleted"}