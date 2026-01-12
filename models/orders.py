from core.database import base
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, date
from sqlalchemy import ForeignKey

class BuyProduct(base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    seller_gmail = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)

    address = Column(ForeignKey("user_address.id"), nullable=False)
    price = Column(Integer, nullable=False)
    pid = Column(Integer, nullable=False)

    mode = Column(String(50))
    status = Column(String(50))

    purchase_date = Column(DateTime, default=datetime.utcnow)
    date_apply = Column(Date)
    delivery_date = Column(Date)