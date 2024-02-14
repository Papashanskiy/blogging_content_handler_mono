import os
import requests

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from pydantic import BaseModel
from social_core.backends.instagram import InstagramOAuth2
from jose import JWTError
from config import config


router = APIRouter()

SOCIAL_AUTH_INSTAGRAM_KEY = config.INSTAGRAM_CLIENT_ID
SOCIAL_AUTH_INSTAGRAM_SECRET = config.INSTAGRAM_CLIENT_SECRET
REDIRECT_URI = "http://localhost:8000/auth/login/callback"  # URL, на который Instagram будет перенаправлять после аутентификации
ACCESS_TOKEN_URL = "https://api.instagram.com/oauth/access_token"

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social_core.backends.instagram.InstagramOAuth2',
)

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"https://api.instagram.com/oauth/authorize?client_id={SOCIAL_AUTH_INSTAGRAM_KEY}&redirect_uri={REDIRECT_URI}&response_type=code"
)


class User(BaseModel):
    username: str


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # В вашем проекте здесь будет проверка токена и возврат пользователя
        # Пока возвращаем заглушку
        return User(username="test_user")
    except JWTError:
        raise credentials_exception


@router.get('/login/callback')
async def login_callback(code: str, response: Response):
    data = {
        'client_id': SOCIAL_AUTH_INSTAGRAM_KEY,
        'client_secret': SOCIAL_AUTH_INSTAGRAM_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': code,
        'grand_type': 'authorization_code'
    }
    response = requests.post(ACCESS_TOKEN_URL, data=data)
    if response.status_code != 200:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Failed to authenticate with Instagram')
    
    # Место для логики
    
    return {'code': code}
