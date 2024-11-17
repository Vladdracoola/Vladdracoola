from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from module_17.app.backend.db_depends import get_db
from typing import Annotated
from module_17.app.models import Task, User
from module_17.app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def get_all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id=int):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task is None:
        raise HTTPException(
            status_code=404,
            detail='Task was not found'
        )
    return task


@router.post('/create')
async def create_tsk(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id=int):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user:
        db.execute(insert(Task).values(title=create_task.title,
                                       content=create_task.content,
                                       priority=create_task.priority,
                                       user_id=user.id))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }

    raise HTTPException(
        status_code=404,
        detail='User was not found'
    )


@router.put('/update')
async def update_tsk(db: Annotated[Session, Depends(get_db)], update_task: UpdateTask, task_id=int):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        db.execute(update(Task).where(Task.id == task_id).values(
            title=update_task.title,
            content=update_task.content,
            priority=update_task.priority))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}
    raise HTTPException(
        status_code=404,
        detail='Task was not found'
    )


@router.delete('/delete')
async def delete_tsk(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}
    raise HTTPException(
        status_code=404,
        detail='Task was not found'
    )
