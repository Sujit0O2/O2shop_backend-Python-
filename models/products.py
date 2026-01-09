from sqlalchemy import Column,String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from core.database import base
class Product(base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    sellername = Column(String)
    status = Column(Integer)
    category = Column(String)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    seller = relationship("User", back_populates="products")
