
from models.orders import BuyProduct
from schemas.addorder_product import BuyProductDTO
from sqlalchemy.orm import Session
from models.users import User

def orderService(req:BuyProductDTO, db:Session,user:dict):
    if(user["role"]!="BUYER"):
        from fastapi import HTTPException,status
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only buyers can place orders"
        )
    
    
    new_order = BuyProduct(**req.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message": "Order created successfully", "order": new_order}
def allorrder_of_user(data:dict,db:Session):
    user=db.query(User).filter(User.email==data["email"]).first()
    return db.query(BuyProduct).filter(BuyProduct.user_id==user.id).all()
    