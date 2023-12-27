from fastapi import FastAPI, Depends, Request
from fastapi.middleware import Middleware
from dotenv import load_dotenv
import uvicorn


load_dotenv()

from routers.client import authenticationRouter
from Database.context import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from middlewares.authorization import checkTokenMiddleWare

app = FastAPI()

app.middleware(CORSMiddleware)
app.middleware("http")(checkTokenMiddleWare)


app.include_router(
    router=authenticationRouter.router,
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@app.get("/")
async def root(request: Request):
    if not request.state.IsAuthenticated:
        return {"message": "Hello World Im Jick Backend\nYou are not authenticated"}
    return {
        "message": f"Hello World Im Jick Backend\nYou are authenticated id: {request.state.userId}"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
