from fastapi import FastAPI,Depends
from dotenv import load_dotenv
from sqlalchemy.orm import Session


load_dotenv()

from routers.client import authenticationRouter
from Database.context import get_db,User


app = FastAPI()

app.include_router(
    router=authenticationRouter.router,
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@app.get("/")
async def root(db:Session = Depends(get_db)):
    return {"message": "Hello World Im Jick Backend"}
