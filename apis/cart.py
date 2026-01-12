from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from core.database import get_db
from models.users import User
from models.products import Product
from models.cart import AddToCart as Cart
from schemas.AddToCartRequest import AddToCartRequest
from core.Security.jwt import get_current_user
from core.Security.jwt import get_current_user

router = APIRouter(
    prefix="/cart",
    tags=["cart"]
,dependencies=[Depends(get_current_user)]
    
)



@router.post("/add")
def add_to_cart(request: AddToCartRequest, db: Session = Depends(get_db),user: dict = Depends(get_current_user)):
    user = db.query(User).filter(User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    product = db.query(Product).filter(Product.id == request.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    cart_item = db.query(Cart).filter(
        Cart.user_id == request.user_id,
        Cart.product_id == request.product_id
    ).first()
    if cart_item:
        cart_item.quantity += request.quantity
    else:
        cart_item = Cart(**request.model_dump()
        )
        db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return {"message": "Product added to cart successfully"}



@router.get("/user/{user_id}", response_model=List[AddToCartRequest])
def get_cart_items(user_id: int, db: Session = Depends(get_db)):
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()
    return cart_items


@router.delete("/remove/{cart_item_id}")
def remove_from_cart(cart_item_id: int, db: Session = Depends(get_db)):
    cart_item = db.query(Cart).filter(Cart.id == cart_item_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    db.delete(cart_item)
    db.commit()
    db.refresh(cart_item)
    
    return {"message": "Item removed from cart successfully"}



@router.put("/update/{cart_item_id}")
def update_cart_item(
    cart_item_id: int,
    quantity: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    cart_item = db.query(Cart).filter(
        Cart.product_id == cart_item_id,
        Cart.user_id == user.id
    ).first()

    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    cart_item.quantity = quantity
    db.commit()

    return {"message": "Cart item updated successfully"}
