
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from Database.context import get_db
from services.client.postsDbServices import addPostForUser, deletePost, getPostsForUser, reactToPost

from schemas.post import CreatePostRequest, GetPostsResponseItem, ReactPostRequest
from fastapi.exceptions import HTTPException as HttpException


router = APIRouter()

@router.post("/create/",response_model=CreatePostRequest)
def create_post(request:Request,text:str,session: Session = Depends(get_db)):
    if request.state.IsAuthenticated:
        post = CreatePostRequest(
            text=text,
            senderId=request.state.userId
        )
        return addPostForUser(post,session)
    else:
          raise HttpException(status_code=401, detail="You are not authenticated")

@router.get("/get/",response_model=GetPostsResponseItem)
def get_post(request:Request,session:Session = Depends(get_db)):
    if request.state.IsAuthenticated:
      return getPostsForUser(request.state.userId,session)
    else:
          raise HttpException(status_code=401, detail="You are not authenticated")
  
@router.get("/delete/{post_id}")
def delete(request:Request,post_id:int,session:Session = Depends(get_db)):
    if request.state.IsAuthenticated:
         if deletePost(post_id,request.state.userId,session):
            return {"message": "The post deleted"}
    else:
          raise HttpException(status_code=401, detail="You are not authenticated")
      

@router.get("/react/{postId}")
def reactPost(request:Request,postId:int,session:Session = Depends(get_db)):
    if request.state.IsAuthenticated:
       reactToPost(request.state.userId,postId,session)
    else:
        raise HttpException(status_code=401, detail="You are not authenticated")

@router.get("/all/")
def getAllPost(request:Request,session:Session = Depends(get_db)):
    if request.state.IsAuthenticated:
       getAllPost(request.state.userId,session)
    else:
        raise HttpException(status_code=401, detail="You are not authenticated")