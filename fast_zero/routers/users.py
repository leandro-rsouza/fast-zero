from http import HTTPStatus
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.security import get_password_hash, get_current_user
from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import UserPublic, UserSchema
from fast_zero.routers.views.users_view import UserView

router = APIRouter(prefix='/users', tags=['users'])

TypeSession = Annotated[Session, Depends(get_session)]
TypeCurrentUser = Annotated[User, Depends(get_current_user)]

class UserController:
    def __init__(self, page):
        self.view = UserView(page)

    @router.post('/create', status_code=HTTPStatus.CREATED, response_model=UserPublic)
    def create_user(user: UserSchema, session: TypeSession, current_user: TypeCurrentUser):
        db_user = session.scalar(
            select(User).where(
                (User.username == user.username) or
                (User.email == user.email)
            )
        )

        if db_user:
            if db_user.username == user.username:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail='Username already exists'
                )
            elif db_user.email == user.email:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail='Email already exists'
                )
            
        db_user = User(
            username=user.username,
            email=user.email,
            password=get_password_hash(user.password),
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    
    def start(self):
        self.view.show_register(self.create_user)