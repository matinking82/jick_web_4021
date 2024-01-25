from fastapi import APIRouter, Depends, Request
from Database.context import get_db
from services.client.userDbServices import (
    followUser,
    getUserProfile,
    isUserActive,
    loginUser,
    updateUserProfile,
)
from schemas.user import UserProfile, UpdateUserProfileModel
from sqlalchemy.orm import Session
from models.user import User
from fastapi.exceptions import HTTPException as HttpException


router = APIRouter()


@router.get("/get/", response_model=UserProfile)
def get_profile(request: Request, session: Session = Depends(get_db)):
    if request.state.IsAuthenticated:
        foundUser = getUserProfile(request.state.userId, session)
        if isUserActive(request.state.userId, session):
            return foundUser
    else:
        raise HttpException(status_code=401, detail="You are not authenticated")


@router.post("/update/", response_model=UserProfile)
def update_profile(
    request: Request,
    update_detail: UpdateUserProfileModel,
    session: Session = Depends(get_db),
):
    print(update_detail)
    if request.state.IsAuthenticated:
        if isUserActive(request.state.userId, session):
            user = updateUserProfile(request.state.userId, update_detail, session)
            return user
    else:
        raise HttpException(status_code=401, detail="You are not authenticated")


@router.post("/Follow/{username}")
def follow(request: Request, username: str, session: Session = Depends(get_db)):
    print(username)
    if request.state.IsAuthenticated:
        if followUser(request.state.userId, username, session):
            return {"message": f"you followed {username}."}
        else:
            raise HttpException(
                status_code=400, detail="there is no user with this username"
            )
    else:
        raise HttpException(status_code=401, detail="You are not authenticated")
