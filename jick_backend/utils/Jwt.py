import os
from jose import jwt, JWTError
import datetime
class JwtPayload:
    id: int
    email: str

    def __init__(self, id: int, email: str):
        self.id = id
        self.email = email

def createJWT(payload: JwtPayload):
    ALGORITHM = "HS256"
    SECRET_KEY = os.environ["JWT_SECRET"]
    expday = 30
    payload.exp = datetime.datetime.utcnow() + datetime.timedelta(days=expday)
    encoded_jwt = jwt.encode(payload.__dict__, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verifyJwt(token: str):
    ALGORITHM = "HS256"
    SECRET_KEY = os.environ["JWT_SECRET"]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        if payload['exp'] < datetime.datetime.utcnow():
            raise JWTError
        
        return payload
    except JWTError:
        return None
