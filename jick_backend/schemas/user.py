from pydantic import BaseModel


class UserRegister(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserProfile(BaseModel):
    username: str
    email: str
    full_name: str
    age: int
    create_date: str

class UpdateUserProfile(BaseModel):
    username: str
    full_name: str
    age: int