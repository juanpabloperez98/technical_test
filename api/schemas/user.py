from pydantic import BaseModel,EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    name: str
    username: str
    email: EmailStr
    password: str

class Login(BaseModel):
    email: EmailStr
    password: str