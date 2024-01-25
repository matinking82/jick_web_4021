from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException as HttpException
from sqlalchemy.orm import Session
from Database.context import get_db
from services.admin.adminDbServices import getAllStats

router = APIRouter()


@router.get("/get")
def stats(request: Request, session: Session = Depends(get_db)):
    if not request.state.IsAdmin:
        raise HttpException(status_code=401, detail="You are not admin")
    
    res = getAllStats(session)
    if res is None:
        raise HttpException(status_code=400, detail="something went wrong")
    return res