from pydantic import BaseModel
class AddToCartRequest(BaseModel):
    user_id: int
    product_id: int
    quantity: int