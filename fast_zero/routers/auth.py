from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.routers.views.login_view import LoginView
from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import Token
from fast_zero.security import verify_password, create_access_token

router = APIRouter(prefix='/auth', tags=['auth'])

TypeSession = Annotated[Session, Depends(get_session)]
TypeOAuth2 = Annotated[OAuth2PasswordRequestForm, Depends()]

class AuthController:
    def __init__(self, page):
        self.view = LoginView(page)

    @router.post('/token', response_model=Token)
    def login_for_access_token(session: TypeSession, form_data: TypeOAuth2):
        
        user = session.scalar(
            select(User).where(User.email == form_data.username)
        )

        if not user or not verify_password(form_data.password, user.password):
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Incorrect email or password'
            )
        
        access_token = create_access_token(data={'sub': user.email})

        return {'access_token': access_token, 'token_type': 'Bearer'}
    
    def login(self):
        self.view.show_login(self.login_for_access_token)