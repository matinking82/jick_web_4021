from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException as HttpException

router = APIRouter()

from services.client import userDbServices
from schemas.user import (
    UserRegister,
    UserLogin,
    forgotPassword,
    forgotPasswordChange,
    ChangePassword,
)
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


@router.post("/forgotPassword")
def forgot_password(forgotPass: forgotPassword, session: Session = Depends(get_db)):
    result = userDbServices.forgotPassword(forgotPass.email, session)
    if result:
        return {"message": "email sent", "temp_guid_token": result}

    raise HttpException(status_code=404, detail="User not found")


@router.post("/changeForgotPassword")
def change_password(
    changeForgottenPassword: forgotPasswordChange, session: Session = Depends(get_db)
):
    result = userDbServices.changeForgottenPassword(changeForgottenPassword, session)
    if result:
        return {"message": "password changed"}

    raise HttpException(status_code=404, detail="User not found")


@router.post("/changePassword")
def change_password(
    request: Request, changePassword: ChangePassword, session: Session = Depends(get_db)
):
    if not request.state.IsAuthenticated:
        raise HttpException(status_code=401, detail="User not authenticated")

    result = userDbServices.changePassword(
        request.state.userId, changePassword, session
    )
    if result:
        return {"message": "password changed"}

    raise HttpException(status_code=404, detail="User not found")
