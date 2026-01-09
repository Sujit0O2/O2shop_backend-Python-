from sqlalchemy.orm import Session
from schemas.AddressCreate import AddressCreate
from models.userAddress import user_address

def add_address(req: AddressCreate, db: Session):

    new_address = user_address(**req.model_dump())

    db.add(new_address)
    db.commit()
    db.refresh(new_address)

    return new_address