from pydantic import BaseModel


class UserRegister(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserProfile(BaseModel):
    username: str | None
    email: str | None
    full_name: str | None
    age: int | None
    create_date: str | None

class UpdateUserProfile(BaseModel):
    username: str
    full_name: str
    age: int
    
class ChangePassword(BaseModel):
    old_password: str
    new_password: str
    
class forgotPasswordChange(BaseModel):
    guid_token: str
    new_password: str
    
class forgotPassword(BaseModel):
    email: str