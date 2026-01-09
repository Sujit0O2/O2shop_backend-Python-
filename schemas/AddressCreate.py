from pydantic import BaseModel
from typing import Optional

class AddressCreate(BaseModel):
    user_id: int
    address_line1: str
    address_line2: Optional[str] = None
    city: str
    state: str
    postal_code: str
    country: str