from pydantic import BaseModel
class login(BaseModel):
    mail:str
    password:str
