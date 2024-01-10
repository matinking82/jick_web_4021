from sqlalchemy.orm import Session
from schemas.post import CreatePostRequest, GetPostsResponseItem
from models.post import Post, PostImage
from models.user import User


def addPostForUser(post: CreatePostRequest, session: Session):
    try:
        newPost = Post(
            id_sender=post.senderId,
            text=post.text,
        )
        session.add(newPost)
        session.commit()
        return newPost
    except Exception as e:
        print(e)


def getPostsForUser(userId: int, session: Session):
    try:
        posts = session.query(Post).filter(Post.id_sender == userId).all()
        if posts is None:
            return []

        result: list[GetPostsResponseItem] = []

        for post in posts:
            item = GetPostsResponseItem(
                id=post.id,
                text=post.text,
                senderId=post.id_sender,
                create_date=post.create_date,
                images=[],
                senderUsername=None,
            )

            sender = session.query(User).filter(User.id == post.id_sender).first()
            images = session.query(PostImage).filter(PostImage.postId == post.id).all()
            
            item.images = [image.imageAdress for image in images]
            item.senderUsername = sender.username
            
            result.append(item)

        return result
    except Exception as e:
        print(e)


def deletePost(postId: int, userId: int, session: Session):
    try:
        post = session.query(Post).filter(Post.id == postId).first()
        if post is None:
            return False

        if post.id_sender == userId:
            session.delete(post)
            session.commit()
            return True

        return False
    except Exception as e:
        print(e)
        return False
