from sqlalchemy.orm import Session
from schemas.product_create import ProductCreate
from models.users import User,Role
from models.products import Product
from fastapi import HTTPException
def addProduct(req:ProductCreate,db:Session):
    seller = db.query(User).filter(User.id == req.seller_id).first()
    if not seller:
        raise HTTPException(status_code=404, detail="Seller not found")

    if seller.role != Role.SELLER:
        raise HTTPException(
            status_code=403,
            detail="Only sellers can add products"
            
        )
        

    product = Product(**req.model_dump())


    db.add(product)
    
    db.commit()
    db.refresh(product)

    return product
