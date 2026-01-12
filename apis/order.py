from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.addorder_product import BuyProductDTO
from services import orderService
from core.Security.jwt import get_current_user

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
def add_order(
    req: BuyProductDTO,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return orderService.orderService(req, db,user)

@router.get("/orders/user/{user_id}")
def get_user_orders(
    user_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return orderService.orderService(db,user)
    
# test ok dont thing bro 
@router.get("/")
def list_orders(
    db: Session = Depends(get_db),
):
    from models.orders import Order

    orders = db.query(Order).all()
    return orders

