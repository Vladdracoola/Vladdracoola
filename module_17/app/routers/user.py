from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from module_17.app.backend.db_depends import get_db
from typing import Annotated
from module_17.app.models import User
from module_17.app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def get_all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id=int):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail='User was not found'
        )
    return user


@router.post('/create')
async def create_usr(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/update')
async def update_usr(db: Annotated[Session, Depends(get_db)], update_user: UpdateUser, user_id=int):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user:
        db.execute(update(User).where(User.id == user_id).values(
            firstname=update_user.firstname,
            lastname=update_user.lastname,
            age=update_user.age))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}
    raise HTTPException(
        status_code=404,
        detail='User was not found'
    )


@router.delete('/delete')
async def delete_usr(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}
    raise HTTPException(
        status_code=404,
        detail='User was not found'
    )
