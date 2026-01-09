from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    stock: int
    category: Optional[str] = None
    status: Optional[int] = 1
    seller_id: int

    