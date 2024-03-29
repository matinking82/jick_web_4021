from fastapi import FastAPI, Depends, Request
from fastapi.middleware import Middleware
from dotenv import load_dotenv
import uvicorn


load_dotenv()

from routers.client import authenticationRouter
from routers.client import userRouter, postRouter
from routers.admin import AdminAuth, StatsRouter, usersManager, postsManager
from Database.context import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from middlewares.authorization import checkTokenMiddleWare, checkAdminMiddleWare

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(checkTokenMiddleWare)
app.middleware("http")(checkAdminMiddleWare)

app.include_router(
    router=authenticationRouter.router,
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

app.include_router(router=userRouter.router, prefix="/user", tags=["profile"])

app.include_router(router=postRouter.router, prefix="/post", tags=["post"])

app.include_router(router=AdminAuth.router, prefix="/admin", tags=["admin"])

app.include_router(router=StatsRouter.router, prefix="/admin/stats", tags=["stats"])

app.include_router(router=usersManager.router, prefix="/admin/user", tags=["users"])

app.include_router(router=postsManager.router, prefix="/admin/post", tags=["posts"])


@app.get("/")
async def root(request: Request):
    if not request.state.IsAuthenticated:
        return {"message": "Hello World Im Jick Backend\nYou are not authenticated"}
    return {
        "message": f"Hello World Im Jick Backend\nYou are authenticated id: {request.state.userId}"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
