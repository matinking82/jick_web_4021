from Database.context import get_db
from models.user import User
from schemas.user import UserRegister, UserLogin
from utils import guidGenerator, passwordHasher
from sqlalchemy.orm import Session


from fastapi import Depends


def registerUser(user: UserRegister, session: Session):
    try:
        newUser = User(
            email=user.email,
            password=passwordHasher.hashPass(user.password),
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
        print(user.email)
        print(foundUser)
        if foundUser is None or not foundUser.is_active:
            return
        
        if passwordHasher.verifyPass(user.password, foundUser.password):
            return foundUser
        
    except Exception as e:
        print(e)