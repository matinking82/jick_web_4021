from fastapi import FastAPI, Depends
from dotenv import load_dotenv

load_dotenv()

from routers.client import authenticationRouter
from Database.context import Base, engine

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
