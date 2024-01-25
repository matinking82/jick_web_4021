from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException as HttpException
from sqlalchemy.orm import Session
from Database.context import get_db
from services.admin.postsDbServices import getAllPostsService,deletePost

router = APIRouter()


@router.get("/get/{page}")
def getAllUsers(request: Request, page: int, session: Session = Depends(get_db)):
    if not request.state.IsAdmin:
        raise HttpException(status_code=401, detail="You are not admin")

    res = getAllPostsService(page, session)
    if res is None:
        raise HttpException(status_code=400, detail="something went wrong")
    return res


@router.post("/delete/{postId}")
def deletePostAction(request: Request, postId: int, session: Session = Depends(get_db)):
    if not request.state.IsAdmin:
        raise HttpException(status_code=401, detail="You are not admin")

    res = deletePost(postId, session)
    if res is None:
        raise HttpException(status_code=400, detail="something went wrong")
    return res
