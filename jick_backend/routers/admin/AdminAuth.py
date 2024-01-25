from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException as HttpException
from sqlalchemy.orm import Session
from Database.context import get_db

from schemas.user import adminLoginRequest
from services.admin.adminDbServices import login
from utils.Jwt import createAdminJWT, AdminJwtPayload

router = APIRouter()


@router.post("/login/")
def register(
    request: Request, logindata: adminLoginRequest, session: Session = Depends(get_db)
):
    res = login(logindata.username, logindata.password, session)
    if res is None:
        raise HttpException(status_code=400, detail="username or password is incorrect")
    plod = AdminJwtPayload()
    plod.id = res.id
    plod.username = res.username
    token = createAdminJWT(plod)

    return {"token": token, "token_type": "bearer"}


@router.get("/validate/")
def validate(request: Request):
    if request.state.IsAdmin:
        return {"message": "you are admin"}

    raise HttpException(status_code=401, detail="You are not admin")
