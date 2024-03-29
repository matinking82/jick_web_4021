from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException as HttpException
from sqlalchemy.orm import Session
from Database.context import get_db
from services.admin.usersDbServices import (
    getAllUsersService,
    ActivateUserService,
    DeActivateUserService,
)

router = APIRouter()


@router.get("/get/{page}")
def getAllUsers(request: Request, page: int, session: Session = Depends(get_db)):
    if not request.state.IsAdmin:
        raise HttpException(status_code=401, detail="You are not admin")

    res = getAllUsersService(page, session)
    if res is None:
        raise HttpException(status_code=400, detail="something went wrong")
    return res


@router.get("/Activate/{userId}")
def ActivateUser(request: Request, userId: int, session: Session = Depends(get_db)):
    if not request.state.IsAdmin:
        raise HttpException(status_code=401, detail="You are not admin")

    res = ActivateUserService(userId, session)
    if res is None:
        raise HttpException(status_code=400, detail="something went wrong")
    return res


@router.get("/DeActivate/{userId}")
def DeActivateUser(request: Request, userId: int, session: Session = Depends(get_db)):
    if not request.state.IsAdmin:
        raise HttpException(status_code=401, detail="You are not admin")

    res = DeActivateUserService(userId, session)
    print(res)
    if res is None:
        raise HttpException(status_code=400, detail="something went wrong")
    return res