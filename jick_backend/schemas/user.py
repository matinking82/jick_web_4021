from pydantic import BaseModel


class UserRegister(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str

class EmailRequest(BaseModel):
    email: str


class UserProfile(BaseModel):
    username: str | None
    email: str | None
    full_name: str | None
    age: int | None
    create_date: str | None
    
class OtherUserProfile(BaseModel):
    username: str | None
    email: str | None
    full_name: str | None
    create_date: str | None
    isFollowing: bool | None

class UpdateUserProfileModel(BaseModel):
    username: str | None
    full_name: str | None
    age: int | None
    
class ChangePassword(BaseModel):
    old_password: str
    new_password: str
    
class forgotPasswordChange(BaseModel):
    guid_token: str
    new_password: str
    
class forgotPassword(BaseModel):
    email: str
    
    
class searchUserResponse(BaseModel):
    username: str
    full_name: str | None
    email: str
    create_date: str
    isFollowing: bool
    
class adminLoginRequest(BaseModel):
    username: str
    password: str