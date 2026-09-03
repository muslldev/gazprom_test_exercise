from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password_hash: str


class UserOut(BaseModel):
    username: str