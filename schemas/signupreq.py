from enum import Enum
from pydantic import BaseModel
from models.users import Role

class signup(BaseModel):
    name: str
    email: str
    password: str
    role: Role
