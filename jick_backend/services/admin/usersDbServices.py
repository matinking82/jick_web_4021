from sqlalchemy.orm import Session
from models.user import User


def getAllUsersService(page: int, session: Session):
    try:
        users = session.query(User).offset(page * 20).limit(20).all()
        return users
    except Exception as e:
        print(e)


def DeActivateUserService(userId: int, session: Session):
    try:
        user = session.query(User).filter(User.id == userId).first()
        if user is None:
            return False

        user.is_active = False
        session.commit()
        return True
    except Exception as e:
        print(e)

def ActivateUserService(userId: int, session: Session):
    try:
        user = session.query(User).filter(User.id == userId).first()
        if user is None:
            return False

        user.is_active = True
        session.commit()
        return True
    except Exception as e:
        print(e)