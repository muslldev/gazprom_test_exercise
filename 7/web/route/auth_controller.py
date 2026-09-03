from typing import Dict
from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from domain.model.auth import AuthRequest, AuthResponse
from domain.model.user import User, UserOut
from domain.service.auth_service import hash_password,verify_password,create_access_token,decode_access_token


auth_router = APIRouter(prefix='/auth',tags=['Auth'])
bearer_scheme = HTTPBearer()

users:Dict[str,User] = {}

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> str:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Невозможно проверить учётные данные",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        username: str | None = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен истёк")
    except jwt.InvalidTokenError:
        raise credentials_exception

    if username not in users:
        raise credentials_exception

    return username


@auth_router.post('/register',response_model=UserOut,status_code=status.HTTP_201_CREATED)
async def register(user:AuthRequest):
    if user.username in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь уже существует"
        )
    
    new_user = User(username=user.username,password_hash=hash_password(user.password))
    users[user.username]=new_user
    return UserOut(username=user.username)

@auth_router.post('/login',response_model=AuthResponse)
async def login(data: AuthRequest):
    user = users.get(data.username)

    if not user or not verify_password(data.password,user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль",
        )

    access_token = create_access_token(data={"sub":user.username})
    return AuthResponse(access_token=access_token)

@auth_router.get('/me',response_model=UserOut)
async def read_current_user(current_user: str = Depends(get_current_user)):
    return UserOut(username=current_user)