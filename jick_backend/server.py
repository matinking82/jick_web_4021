from fastapi import FastAPI,Depends
from dotenv import load_dotenv


load_dotenv()

from models import *
from routers.client import authenticationRouter
from Database.context import Base,engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(
    router=authenticationRouter.router,
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@app.get("/")
async def root():
    return {"message": "Hello World Im Jick Backend"}
