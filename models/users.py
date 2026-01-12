from core.database import base
from enum import Enum
from sqlalchemy import Column,String,Integer,Enum as saEnum
from sqlalchemy.orm import relationship
class Role(Enum):
    BUYER="BUYER"
    SELLER="SELLER"

class User(base):
    __tablename__="users"
    id=Column(Integer,index=True,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
    role=Column(saEnum(Role),nullable= False)
    password=Column(String,nullable= False)
    # orders = relationship("orders", back_populates="buyer")
    products = relationship("Product", back_populates="seller")