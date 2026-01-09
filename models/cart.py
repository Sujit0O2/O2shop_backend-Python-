
from sqlalchemy import Column, Integer, String
from core.database import base
class AddToCart(base):
    __tablename__ = "cart"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)