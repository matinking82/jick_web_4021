from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from Database.context import  get_db
from services.client.userDbServices import getUserProfile, isUserActive, loginUser, updateUserProfile
from schemas.user import UpdateUserProfile, UserLogin, UserProfile
from sqlalchemy.orm import Session
from models.user import User
from fastapi.exceptions import HTTPException as HttpException



router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/prfile/{user_id}",response_model=UserProfile)
def get_profile(user_id:int,session: Session = Depends(get_db)):
     foundUser = getUserProfile(user_id,session)
     if isUserActive(user_id,session):
          return foundUser

@router.post("/profile/update/{user_id}",response_model=UserProfile)
def update_profile(user_id:int,update_detail:UpdateUserProfile,session: Session = Depends(get_db)):
     if isUserActive(user_id,session):
         user= updateUserProfile(user_id,update_detail,session)
         return user
