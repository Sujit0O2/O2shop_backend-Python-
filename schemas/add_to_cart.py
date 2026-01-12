from pydantic import BaseModel

class AddToCart(BaseModel):
    id: int
    user_mail: str
    pid: int
    quantity: int   
    