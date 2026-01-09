from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class BuyProductDTO(BaseModel):
    user_id: int
    seller_gmail: str
    quantity: int

    address: int
    price: int
    pid: int

    mode: Optional[str] = None
    status: Optional[str] = None

    purchase_date: Optional[datetime] = None
    date_apply: Optional[date] = None
    delivery_date: Optional[date] = None