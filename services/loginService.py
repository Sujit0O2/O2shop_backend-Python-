from sqlalchemy.orm import Session
from schemas.loginreq import login
from models.users import User
from passlib.context import CryptContext

context = CryptContext(schemes=["argon2"], deprecated="auto")

def CheckUser(sq: login, db: Session):
    user = (
        db.query(User)
        .filter(User.email == sq.mail)
        .first()
    )

    if not user:
        return None

    if not context.verify(sq.password, user.password):
        return None

    return user
