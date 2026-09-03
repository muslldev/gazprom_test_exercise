from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr

class User(BaseModel):
    id: UUID
    name: str
    email: EmailStr

    class Config:
        json_encoders = {
            uuid4: str
        }

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None