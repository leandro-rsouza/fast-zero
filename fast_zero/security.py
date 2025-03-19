from http import HTTPStatus
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jwt import encode, decode
from jwt.exceptions import PyJWTError
from pwdlib import PasswordHash

from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.settings import Settings
from fast_zero.models import User

settings = Settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')

pwd_context = PasswordHash.recommended()

TypeSession = Annotated[Session, Depends(get_session)]
TypeOAuth2 = Annotated[str, Depends(oauth2_scheme)]

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed: str):
    return pwd_context.verify(plain_password, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(
        tz=ZoneInfo('UTC') + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRES_MINUTES
        )
    )

    to_encode.update({'exp': expire})

    encoded_jwt = encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return encoded_jwt

def currente_user(session: TypeSession, token: TypeOAuth2):
    
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get('sub')
        
        if not username:
            raise credentials_exception
        
    except PyJWTError:
        raise credentials_exception
    
    user = session.scalar(
        select(User).where(User.email == username)
    )

    if not user:
        raise credentials_exception
    
    return user