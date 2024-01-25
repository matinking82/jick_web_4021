from sqlalchemy.orm import Session
from schemas.post import (
    CreatePostRequest,
    GetPostsResponseItem,
    ReactPostRequest,
    PostResponse,
)
from models.post import Post, PostImage
from models.user import User, UserFollow
from models.postReaction import postReaction


def addPostForUser(post: CreatePostRequest, session: Session):
    try:
        newPost = Post(
            id_sender=post.senderId,
            text=post.text,
        )
        session.add(newPost)
        session.commit()

        sender: User = session.query(User).filter(User.id == newPost.id_sender).first()

        resPost = PostResponse(
            id=newPost.id,
            text=newPost.text,
            senderId=newPost.id_sender,
            create_date=str(newPost.create_date),
            senderEmail=sender.email,
            likes=0,
        )

        return resPost
    except Exception as e:
        print(e)


def getPostsForUser(userId: int, session: Session):
    try:
        posts = session.query(Post).filter(Post.id_sender == userId).all()
        if posts is None:
            return []

        result: list[PostResponse] = []
        
        for post in posts:
            sender: User = session.query(User).filter(User.id == post.id_sender).first()
            likes = (
                session.query(postReaction)
                .filter(postReaction.postId == post.id)
                .filter(postReaction.can_like == True)
                .all()
            )
            resPost = PostResponse(
                id=post.id,
                text=post.text,
                senderId=post.id_sender,
                create_date=str(post.create_date),
                senderEmail=sender.email,
                likes=len(likes),
            )
            result.append(resPost)        
        
        return result
    except Exception as e:
        print(e)

def getPostsForUsername(email: str, session: Session):
    try:
        user = session.query(User).filter(User.email == email).first()
        if user is None:
            return []
        posts = session.query(Post).filter(Post.id_sender == user.id).all()
        if posts is None:
            return []

        result: list[PostResponse] = []
        
        for post in posts:
            sender: User = session.query(User).filter(User.id == post.id_sender).first()
            likes = (
                session.query(postReaction)
                .filter(postReaction.postId == post.id)
                .filter(postReaction.can_like == True)
                .all()
            )
            resPost = PostResponse(
                id=post.id,
                text=post.text,
                senderId=post.id_sender,
                create_date=str(post.create_date),
                senderEmail=sender.email,
                likes=len(likes),
            )
            result.append(resPost)        
        
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


def reactToPost(userId: int, postId: int, session: Session):
    try:
        post = session.query(Post).filter(Post.id == postId).first()

        if post is None:
            return False

        postReactioncreate = (
            session.query(postReaction)
            .filter(postReaction.postId == postId)
            .filter(postReaction.userId == userId)
            .first()
        )

        if postReactioncreate is None:
            postReactioncreate = postReaction(
                postId=postId, userId=userId, can_like=True
            )
            session.add(postReactioncreate)
        else:
            return False

        session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def getAllPost(userId: int, session: Session):
    try:
        all_post: list[Post] = list()
        users = session.query(UserFollow).filter(UserFollow.followerId == userId).all()
        if users is None:
            return
        for user in users:
            posts = session.query(Post).filter(Post.id_sender == user.followingId).all()
            all_post.append(posts)

        # flatten list
        all_post = [y for x in all_post for y in x]

        # remove duplicate
        all_post = list(dict.fromkeys(all_post))

        # sort by date newest to oldest
        all_post.sort(key=lambda x: x.create_date, reverse=True)

        resAll: list[PostResponse] = list()

        for post in all_post:
            sender: User = session.query(User).filter(User.id == post.id_sender).first()
            likes = (
                session.query(postReaction)
                .filter(postReaction.postId == post.id)
                .filter(postReaction.can_like == True)
                .all()
            )
            resPost = PostResponse(
                id=post.id,
                text=post.text,
                senderId=post.id_sender,
                create_date=str(post.create_date),
                senderEmail=sender.email,
                likes=len(likes),
            )
            resAll.append(resPost)

        return resAll

    except Exception as e:
        print(e)
        return False


def getRecentPosts(session: Session):
    try:
        all_post: list[Post] = list()
        posts = session.query(Post).all()
        all_post.append(posts)

        # flatten list
        all_post = [y for x in all_post for y in x]

        # remove duplicate
        all_post = list(dict.fromkeys(all_post))

        # sort by date newest to oldest
        all_post.sort(key=lambda x: x.create_date, reverse=True)

        resAll: list[PostResponse] = list()
        for post in all_post[:20]:  # Limit to 20 posts
            sender: User = session.query(User).filter(User.id == post.id_sender).first()
            likes = (
                session.query(postReaction)
                .filter(postReaction.postId == post.id)
                .filter(postReaction.can_like == True)
                .all()
            )
            resPost = PostResponse(
                id=post.id,
                text=post.text,
                senderId=post.id_sender,
                create_date=str(post.create_date),
                senderEmail=sender.email,
                likes=len(likes),
            )
            resAll.append(resPost)

        return resAll
    except Exception as e:
        print(e)