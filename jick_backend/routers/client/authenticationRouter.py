from fastapi import APIRouter
router = APIRouter()

@router.post("/register")
def user_register():
    return {"message": "Hello World"}


@router.post("/activate")
def user_login():
    return {"message": "Hello World"}