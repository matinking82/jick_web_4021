from sqlalchemy.orm import Session
from models.post import Post
from models.postReaction import postReaction
from models.user import User
from schemas.post import PostResponse


def getAllPostsService(page: int, session: Session):
    try:
        posts = session.query(Post).offset(page * 20).limit(20).all()
        resPosts: list[PostResponse] = []
        for post in posts:
            sender = session.query(User).filter(User.id == post.id_sender).first()
            likes = (
                session.query(postReaction)
                .filter(postReaction.postId == post.id)
                .filter(postReaction.can_like == True)
                .all()
            )
            resPosts.append(
                PostResponse(
                    id=post.id,
                    text=post.text,
                    senderId=post.id_sender,
                    create_date=str(post.create_date),
                    senderEmail=sender.email,
                    likes=len(likes),
                )
            )
        return resPosts
    except Exception as e:
        print(e)


def deletePost(postId: int, session: Session):
    try:
        post = session.query(Post).filter(Post.id == postId).first()
        if post is None:
            return False

        session.delete(post)
        session.commit()
        return True
    except Exception as e:
        print(e)
