from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.Security.jwt import get_current_user
from services.add_address import add_address
from schemas.AddressCreate import AddressCreate
router = APIRouter(prefix="/addresses", tags=["Addresses"])
@router.post(
    "/address",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_user)]
)
def create_address(
    req: AddressCreate,
    db: Session = Depends(get_db)
):
    address = add_address(req, db)
    if not address:
        raise HTTPException(status_code=400, detail="Failed to add address")
    return address

@router.delete("/{address_id}")
def delete_address(
    address_id: int,
    db: Session = Depends(get_db),
):
    from models.userAddress import user_address

    address = db.query(user_address).filter(user_address.id == address_id).first()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    db.delete(address)
    db.commit()

    return {"message": "Address deleted successfully"}

@router.get("/user/{user_id}")
def get_user_addresses(
    user_id: int,
    db: Session = Depends(get_db),
):
    from models.userAddress import user_address

    addresses = db.query(user_address).filter(user_address.user_id == user_id).all()

    return addresses

@router.put("/{address_id}")
def update_address(
    address_id: int,
    req: AddressCreate,
    db: Session = Depends(get_db),
):
    from models.userAddress import user_address

    address = db.query(user_address).filter(user_address.id == address_id).first()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    for field, value in req.model_dump(exclude_unset=True).items():
        setattr(address, field, value)

    db.commit()
    db.refresh(address)

    return address

