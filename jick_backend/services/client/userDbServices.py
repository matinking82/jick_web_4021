from models.user import User, UserFollow
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
        newUser.is_active = True

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
def getUserProfile(user_id: int, session: Session):
    try:
        foundUser = session.query(User).filter(User.id == user_id).first()
        if foundUser is None:
            return
        result = UserProfile(
            username=foundUser.username,
            email=foundUser.email,
            full_name=foundUser.full_name,
            age=foundUser.age,
            create_date=str(foundUser.create_date),
        )
        return result
    except Exception as e:
        print(e)


def getUserProfileByUsername(userId: int, email: str, session: Session):
    try:
        foundUser = session.query(User).filter(User.email == email).first()
        if foundUser is None:
            return

        isfollowing = (
            session.query(UserFollow)
            .filter(UserFollow.followerId == userId)
            .filter(UserFollow.followingId == foundUser.id)
            .first()
        )
        if isfollowing is None:
            isfollowing = False
        else:
            isfollowing = True

        result = OtherUserProfile(
            username=foundUser.username,
            email=foundUser.email,
            full_name=foundUser.full_name,
            create_date=str(foundUser.create_date),
            isFollowing=isfollowing,
        )
        return result
    except Exception as e:
        print(e)


def updateUserProfile(user_id: int, user: UpdateUserProfileModel, session: Session):
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
            email=foundUser.email,
            full_name=foundUser.full_name,
            age=foundUser.age,
            create_date=str(foundUser.create_date),
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


def forgotPasswordWithEmail(user_email: str, session: Session):
    try:
        foundUser = session.query(User).filter(User.email == user_email).first()
        if foundUser is None:
            return
        foundUser.guid_token = guidGenerator.generateGUID()
        session.commit()
        return foundUser.guid_token
    except Exception as e:
        print(e)


def changeForgottenPassword(user: forgotPasswordChange, session: Session):
    try:
        foundUser = (
            session.query(User).filter(User.guid_token == user.guid_token).first()
        )
        if foundUser is None:
            return
        foundUser.password = passwordHasher.hashPass(user.new_password)
        session.commit()
        return foundUser
    except Exception as e:
        print(e)


def followUser(user_id: int, username: str, session: Session):
    try:
        foundUser = session.query(User).filter(User.id == user_id).first()
        if foundUser is None:
            return
        userToFollow = session.query(User).filter(User.username == username).first()
        if userToFollow is None:
            return

        if userToFollow.id == user_id:
            return
        # check if followed before

        follow = (
            session.query(UserFollow)
            .filter(UserFollow.followerId == user_id)
            .filter(UserFollow.followingId == userToFollow.id)
            .first()
        )

        if follow is not None:
            return

        follow = UserFollow(followerId=user_id, followingId=userToFollow.id)
        session.add(follow)
        session.commit()
        return True

    except Exception as e:
        print(e)
        return False


def unfollowUser(user_id: int, username: str, session: Session):
    try:
        foundUser = session.query(User).filter(User.id == user_id).first()
        if foundUser is None:
            return
        userToFollow = session.query(User).filter(User.username == username).first()
        if userToFollow is None:
            return

        # check if followed before

        follow = (
            session.query(UserFollow)
            .filter(UserFollow.followerId == user_id)
            .filter(UserFollow.followingId == userToFollow.id)
            .first()
        )

        if follow is None:
            return

        session.delete(follow)
        session.commit()
        return True

    except Exception as e:
        print(e)
        return False


def followUserByEmail(user_id: int, email: str, session: Session):
    try:
        foundUser = session.query(User).filter(User.id == user_id).first()
        if foundUser is None:
            return
        userToFollow = session.query(User).filter(User.email == email).first()
        if userToFollow is None:
            return

        if userToFollow.id == user_id:
            return
        # check if followed before

        follow = (
            session.query(UserFollow)
            .filter(UserFollow.followerId == user_id)
            .filter(UserFollow.followingId == userToFollow.id)
            .first()
        )

        if follow is not None:
            return

        follow = UserFollow(followerId=user_id, followingId=userToFollow.id)
        session.add(follow)
        session.commit()
        return True

    except Exception as e:
        print(e)
        return False


def unfollowUserByEmail(user_id: int, email: str, session: Session):
    try:
        foundUser = session.query(User).filter(User.id == user_id).first()
        if foundUser is None:
            return
        userToFollow = session.query(User).filter(User.email == email).first()
        if userToFollow is None:
            return
        
        print(userToFollow.id)
        print(user_id)

        # check if followed before

        follow = (
            session.query(UserFollow)
            .filter(UserFollow.followerId == user_id)
            .filter(UserFollow.followingId == userToFollow.id)
            .first()
        )

        if follow is None:
            return

        session.delete(follow)
        session.commit()
        return True

    except Exception as e:
        print(e)
        return False


def searchUserServicce(searcherId: int, search_key: str, session: Session):
    try:
        users = session.query(User).filter(User.username.ilike(f"%{search_key}%")).all()
        resUsers: list[searchUserResponse] = list()

        for user in users:
            isFollowing = (
                session.query(UserFollow)
                .filter(UserFollow.followerId == searcherId)
                .filter(UserFollow.followingId == user.id)
                .first()
            )
            if isFollowing is None:
                isFollowing = False
            else:
                isFollowing = True
            resUsers.append(
                searchUserResponse(
                    username=user.username,
                    full_name=user.full_name,
                    email=user.email,
                    create_date=str(user.create_date),
                    isFollowing=isFollowing,
                )
            )

        return resUsers
    except Exception as e:
        print(e)
        return []
