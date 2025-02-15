from fastapi import APIRouter, Depends, status
from models.task import Task
from typing import Annotated, Optional
from sqlalchemy.orm import Session
from database import get_session
from pydantic import BaseModel


router = APIRouter()

# Dependency injection
db_dependency = Annotated[Session, Depends(get_session)]


class TaskRequest(BaseModel):
    name: str
    bucket_id: Optional[int] = None
    description: Optional[str] = None
    completed: bool = False
    start_at: Optional[str] = None
    end_at: Optional[str] = None


@router.get("/", status_code=status.HTTP_200_OK)
async def read_tasks(db: db_dependency):
    task_models = db.query(Task).all()

    return task_models


@router.get("/{task_id}", status_code=status.HTTP_200_OK)
async def read_task(db: db_dependency, task_id: int):
    task_model = db.query(Task).filter(Task.id == task_id).first()

    return task_model


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(db: db_dependency, task_request: TaskRequest):
    task_model = Task(
        name=task_request.name,
        bucket_id=task_request.bucket_id,
        description=task_request.description,
        completed=task_request.completed,
        start_at=task_request.start_at,
        end_at=task_request.end_at,
    )
    db.add(task_model)
    db.commit()
    
    
@router.put("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_task(task_id: int, db: db_dependency, task_request: TaskRequest):
    task_model = db.query(Task).filter(Task.id == task_id).first()
    task_model.name = task_request.name
    task_model.bucket_id = task_request.bucket_id
    task_model.completed = task_request.completed
    task_model.description = task_request.description
    task_model.start_at = task_request.start_at
    task_model.end_at = task_model.end_at
    
    

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: db_dependency):
    db.query(Task).filter(Task.id == task_id).delete()
    db.commit()
