from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from core.Security.jwt import get_current_user
from models.users import Role

from models.products import Product
from models.users import User
from schemas.product_create import ProductCreate
from services.productService import addProduct

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# ----------------------------
# CREATE PRODUCT (SELLER ONLY)
# ----------------------------
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(
    req: ProductCreate,
    db: Session = Depends(get_db),
):
    return addProduct(
        req=req,
        db=db,
    )



@router.put("/{product_id}")
def update_product(
    product_id: int,
    product_data: ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    sellerid=product.seller_id
    seller=db.query(User).filter(User.id==sellerid).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if sellerid !=seller.id or user["role"] != "SELLER":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed"
        )

    for field, value in product_data.model_dump(exclude_unset=True).items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)
    return product



@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    sellerid=product.seller_id
    seller=db.query(User).filter(User.id==sellerid).first()
    

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if sellerid !=seller.id or user["role"] != "SELLER":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed"
        )

    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}



@router.get("/")
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/by_category/{category}")
def get_products_by_category(category: str, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.category == category).all()


@router.get("/by_seller/{seller_id}")
def get_products_by_seller(seller_id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.seller_id == seller_id).all()
