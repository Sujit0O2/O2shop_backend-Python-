from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from schemas.signupreq import signup
from schemas.loginreq import login
from core.database import get_db

from services.loginService import CheckUser
from services.signupService import AddUser
from core.Security.jwt import create_access_token

route = APIRouter(prefix="/user", tags=["auth"])


@route.post("/login")
def login_user(
    req: login,
    response: Response,
    db: Session = Depends(get_db)
):
    user = CheckUser(req, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token({
        "user_id": user.id,
        "email": user.email,
        "role": user.role.name  # if role is a relationship
    })

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,      # ⚠️ set False in local dev if no HTTPS
        samesite="lax",
        max_age=60 * 60
    )

    return {"message": "Login successful"}

@route.post("/signup")
def sign_up(req: signup, db: Session = Depends(get_db)):
    user = AddUser(req, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    return {"message": "User successfully created"}
