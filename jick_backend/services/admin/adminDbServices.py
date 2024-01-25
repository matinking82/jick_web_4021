from sqlalchemy.orm import Session
from models.admin import admin
from models.user import *
from models.post import *
from models.postReaction import *

from schemas.stats import *
from utils.passwordHasher import verifyPass, hashPass


def login(username: str, password: str, session: Session):
    try:
        # if there is no admin add admin admin
        if session.query(admin).first() is None:
            newAdmin = admin(username="admin", password=hashPass("admin"))
            session.add(newAdmin)
            session.commit()

        foundAdmin = session.query(admin).filter(admin.username == username).first()

        if foundAdmin is None:
            return

        if verifyPass(password, foundAdmin.password):
            return foundAdmin

        return
    except Exception as e:
        print(e)


def getAllStats(session: Session):
    try:
        stats = statistics()

        stats.total_registers = session.query(User).count()
        stats.total_posts = session.query(Post).count()
        stats.total_likes = session.query(postReaction).count()
        stats.total_follows = session.query(UserFollow).count()

        # stats for last month
        stats.new_posts = (
            session.query(Post)
            .filter(
                Post.create_date
                >= datetime.datetime.now() - datetime.timedelta(days=30)
            )
            .count()
        )
        stats.new_follows = (
            session.query(UserFollow)
            .filter(
                UserFollow.create_date
                >= datetime.datetime.now() - datetime.timedelta(days=30)
            )
            .count()
        )
        stats.new_registers = (
            session.query(User)
            .filter(
                User.create_date
                >= datetime.datetime.now() - datetime.timedelta(days=30)
            )
            .count()
        )
        return stats
    except Exception as e:
        print(e)
