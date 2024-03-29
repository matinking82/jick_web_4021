from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from Database.context import get_db
from services.client.userDbServices import (
    followUser,
    getUserProfile,
    isUserActive,
    loginUser,
    updateUserProfile,
    unfollowUser,
    searchUserServicce,
    getUserProfileByUsername,
    followUserByEmail,
    unfollowUserByEmail,
)
from schemas.user import UserProfile, UpdateUserProfileModel, OtherUserProfile,EmailRequest
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


@router.get("/get/{email}", response_model=OtherUserProfile)
def get_profile_by_username(
    request: Request, email: str, session: Session = Depends(get_db)
):
    if not request.state.IsAuthenticated:
        raise HttpException(status_code=401, detail="You are not authenticated")

    res = getUserProfileByUsername(request.state.userId, email, session)
    if res is None:
        raise HttpException(
            status_code=400, detail="there is no user with this username"
        )
    return res


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


@router.post("/unFollow/{username}")
def unFollow(request: Request, username: str, session: Session = Depends(get_db)):
    print(username)
    if request.state.IsAuthenticated:
        res = unfollowUser(request.state.userId, username, session)
        if res is None or not res:
            raise HttpException(
                status_code=400, detail="you are not following this user"
            )
        return {"message": f"you unfollowed {username}."}
    else:
        raise HttpException(status_code=401, detail="You are not authenticated")




@router.post("/eFollow/")
def eFollow(request: Request, email: EmailRequest, session: Session = Depends(get_db)):
    if request.state.IsAuthenticated:
        if followUserByEmail(request.state.userId, email.email, session):
            return {"message": f"you followed {email.email}."}
        else:
            raise HttpException(
                status_code=400, detail="there is no user with this email"
            )
    else:
        raise HttpException(status_code=401, detail="You are not authenticated")


@router.post("/eUnFollow/")
def eUnFollow(
    request: Request, email: EmailRequest, session: Session = Depends(get_db)
):
    if request.state.IsAuthenticated:
        res = unfollowUserByEmail(request.state.userId, email.email, session)
        if res is None or not res:
            raise HttpException(
                status_code=400, detail="you are not following this user"
            )
        return {"message": f"you unfollowed {email.email}."}
    else:
        raise HttpException(status_code=401, detail="You are not authenticated")


@router.post("/search/{search_key}")
def searchUser(request: Request, search_key: str, session: Session = Depends(get_db)):
    if request.state.IsAuthenticated:
        res = searchUserServicce(request.state.userId, search_key, session)
        if res is None:
            raise HttpException(
                status_code=400, detail="something went wrong, try again later"
            )
        return res
    else:
        raise HttpException(status_code=401, detail="You are not authenticated")
