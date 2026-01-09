from sqlalchemy import Column, Integer, String, DateTime
from core.database import base
from sqlalchemy import ForeignKey

class user_address(base):
    __tablename__ = "user_address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id =Column(ForeignKey("users.id"), nullable=False)
    address_line1 = Column(String(255), nullable=False)
    address_line2 = Column(String(255))
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    country = Column(String(100), nullable=False)
