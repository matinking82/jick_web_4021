from fastapi import APIRouter, Depends,Request
from fastapi.security import OAuth2PasswordBearer
from Database.context import  get_db
from services.client.userDbServices import getUserProfile, isUserActive, loginUser, updateUserProfile
from schemas.user import UpdateUserProfile, UserLogin, UserProfile
from sqlalchemy.orm import Session
from models.user import User
from fastapi.exceptions import HTTPException as HttpException



router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/get/",response_model=UserProfile)
def get_profile(request:Request,session: Session = Depends(get_db)):
     if request.state.IsAuthenticated:
          foundUser = getUserProfile(request.state.userId,session)
          if isUserActive(request.state.userId,session):
               return foundUser
     else:
          raise HttpException(status_code=401, detail="You are not authenticated")

@router.post("/update/",response_model=UserProfile)
def update_profile(request:Request,update_detail:UpdateUserProfile,session: Session = Depends(get_db)):
     if request.state.IsAuthenticated:
          if isUserActive(request.state.userId,session):
               user= updateUserProfile(request.state.userId,update_detail,session)
               return user
     else:
          raise HttpException(status_code=401, detail="You are not authenticated")