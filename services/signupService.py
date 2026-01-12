from sqlalchemy.orm import Session
from passlib.context import CryptContext
from schemas.signupreq import signup
from models.users import User

context = CryptContext(schemes=["argon2"])

def AddUser(sq: signup, db: Session):
    email = sq.email.lower().strip()

    ext_user = db.query(User).filter(User.email == email).first()
    if ext_user:
        return None

    user = User(**sq.model_dump())
    user.email = email

    user.password = context.hash(sq.password)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user
