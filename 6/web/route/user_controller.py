from typing import List
from uuid import UUID, uuid4
from fastapi import APIRouter, HTTPException,status
from service.model.user import User, UserCreate, UserUpdate


user_router = APIRouter(prefix='/users',tags=['Users'])

users: List[User] = [
    User(
        id=uuid4(),
        name='John',
        email='john@example.com',
    ),
    User(
        id=uuid4(),
        name='Daisy',
        email='daisy@example.com',
    ),
    User(
        id=uuid4(),
        name='Angela',
        email='angela@example.com',
    )
]

@user_router.post('/',status_code=201)
async def create_user(data:UserCreate):
    for u in users:
        if u.name == data.name:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Пользователь с именем '{data.name}' уже существует"
            )
        if u.email == data.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Пользователь с email '{data.email}' уже существует"
            )
        
    user = User(
        id=uuid4(),
        name=data.name,
        email=data.email
    )
    
    users.append(user)
    return {"status": "Пользователь создан"}

@user_router.get('/',response_model=List[User])
async def get_users():
    return users

@user_router.get('/{user_id}',response_model=User)
async def get_user_by_id(user_id:UUID):
    for u in users:
        if u.id == user_id:
            return u
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Пользователь с ID {user_id} не найден"
    )

@user_router.put('/{user_id}',status_code=status.HTTP_200_OK,response_model=User)
async def update_user(user_id:UUID, data:UserUpdate):
    user = None
    user_index = None

    for i,u in enumerate(users):
        if u.id == user_id:
            user = u
            user_index = i
            break

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Пользователь с ID {user_id} не найден"
        )

    if data.name:
        for u in users:
            if u.id != user_id and u.name == data.name:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"Пользователь с именем '{data.name}' уже существует"
                )

    if data.email:
            for u in users:
                if u.id != user_id and u.email == data.email:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail=f"Пользователь с email '{data.email}' уже существует"
                    )

    updated_user = User(
        id=user_id,
        name=data.name if data.name is not None else user.name,
        email=data.email if data.email is not None else user.email
    )

    users[user_index] = updated_user
    
    return updated_user
    

@user_router.delete('/{user_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id:UUID):
    for i,u in enumerate(users):
        if u.id == user_id:
            users.pop(i)
            return {"status":"Пользователь удалён"}
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Пользователь с ID {user_id} не найден"
    )