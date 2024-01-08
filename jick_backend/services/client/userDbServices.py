from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from Database.context import get_db
from models.user import User
from schemas.user import *
from utils import guidGenerator, passwordHasher
from sqlalchemy.orm import Session

# user auth
def registerUser(user: UserRegister, session: Session):
    try:
        current_user = user
        user = session.query(User).filter(User.email == user.email).first()
        if user is not None:
            if user.is_active:
                return
            else: 
                # delete
                current_user = user
                session.delete(user)
                session.commit()

        newUser = User(
            email=current_user.email,
            password=passwordHasher.hashPass(current_user.password),
            guid_token=guidGenerator.generateGUID(),
        )
        session.add(newUser)
        session.commit()
        return newUser

    except Exception as e:
        print(e)


def activateUser(guid_token: str, session: Session):
    try:
        user = session.query(User).filter(User.guid_token == guid_token).first()
        if user is None:
            return False
        user.is_active = True
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def loginUser(user: UserLogin, session: Session):
    try:
        foundUser = session.query(User).filter(User.email == user.email).first()
        if foundUser is None or not foundUser.is_active:
            return

        if passwordHasher.verifyPass(user.password, foundUser.password):
            return foundUser

    except Exception as e:
        print(e)


def isUserActive(user_id: int, session: Session):
    try:
        foundUser = session.query(User).filter(User.id == user_id).first()
        if foundUser is None:
            return False
        return foundUser.is_active
    except Exception as e:
        print(e)
        return False


# user profile
def getUserProfile(user_id:int, session: Session):
    try:
        foundUser = session.query(User).filter(User.id == user_id).first()
        if foundUser is None:
            return
        result = UserProfile(
            username = foundUser.username,
            email= foundUser.email,
            full_name=foundUser.full_name,
            age = foundUser.age,
            create_date= str(foundUser.create_date)            
        )
        return result
    except Exception as e:
        print(e)

def updateUserProfile(user_id: int, user: UpdateUserProfile, session: Session):
    try:
        foundUser = session.query(User).filter(User.id == user_id).first()
        if foundUser is None:
            return
        foundUser.username = user.username
        foundUser.full_name = user.full_name
        foundUser.age = user.age
        session.commit()

        result = UserProfile(
            username=foundUser.username,
            email= foundUser.email,
            full_name = foundUser.full_name,
            age = foundUser.age,
            create_date= str(foundUser.create_date)
     
        )
        return result
    except Exception as e:
        print(e)


def changePassword(user_id: int, user: ChangePassword, session: Session):
    try:
        foundUser = session.query(User).filter(User.id == user_id).first()
        if foundUser is None:
            return
        if not passwordHasher.verifyPass(user.old_password, foundUser.password):
            return
        foundUser.password = passwordHasher.hashPass(user.new_password)
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def forgotPassword(user_id: int, session: Session):
    try:
        foundUser = session.query(User).filter(User.id == user_id).first()
        if foundUser is None:
            return
        foundUser.guid_token = guidGenerator.generateGUID()
        session.commit()
        return foundUser.guid_token
    except Exception as e:
        print(e)


def changeForgottenPassword(user:forgotPasswordChange, session: Session):
    try:
        foundUser = session.query(User).filter(User.guid_token == user.guid_token).first()
        if foundUser is None:
            return
        foundUser.password = passwordHasher.hashPass(user.new_password)
        session.commit()
        return foundUser
    except Exception as e:
        print(e)
