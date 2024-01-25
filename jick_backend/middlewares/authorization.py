from utils.Jwt import verifyJwt,verifyAdminJwt
import services.client.userDbServices as userDbServices
from fastapi import HTTPException, status,Request

async def checkTokenMiddleWare(request: Request, call_next):
    request.state.IsAuthenticated = False
    token = request.headers.get("Authorization", "").replace("Bearer ", "")

    if token == "":
        return await call_next(request)

    try:
        user = verifyJwt(token)
    except:
        return await call_next(request)

    if user is None:
        return await call_next(request)

    request.state.userId = user.id
    request.state.IsAuthenticated = True

    return await call_next(request)

async def checkAdminMiddleWare(request: Request, call_next):
    request.state.IsAdmin = False
    token = request.headers.get("Authorization", "").replace("Bearer ", "")

    if token == "":
        return await call_next(request)

    try:
        user = verifyAdminJwt(token)
    except:
        return await call_next(request)

    if user is None:
        return await call_next(request)

    request.state.userId = user.id
    request.state.IsAdmin = True

    return await call_next(request)