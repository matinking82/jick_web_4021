from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException as HttpException

router = APIRouter()

from services.client import userDbServices
from schemas.user import UserRegister, UserLogin
from sqlalchemy.orm import Session
from Database.context import get_db
from utils import email, Jwt


@router.post("/register")
def user_register(user: UserRegister, session: Session = Depends(get_db)):
    result = userDbServices.registerUser(user, session)
    if result:
        email.sendVerificationEmail(result.email, result.guid_token)

        return {"message": "user registered now you have to activate your account"}

    raise HttpException(status_code=500, detail="something went wrong")


@router.get("/activate/{guid_token}")
def user_activate(guid_token: str, session: Session = Depends(get_db)):
    if userDbServices.activateUser(guid_token, session):
        return {"message": "user activated"}

    raise HttpException(status_code=400, detail="activation failed")


@router.post("/login")
def user_login(user: UserLogin, session: Session = Depends(get_db)):
    result = userDbServices.loginUser(user, session)
    if not result:
        raise HttpException(status_code=404, detail="User not found")

    plod = Jwt.JwtPayload()
    plod.id = result.id
    plod.email = result.email
    
    token = Jwt.createJWT(plod)

    return {"token": token, "token_type": "bearer"}
