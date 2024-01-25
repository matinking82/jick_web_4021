from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    text: str
    senderId: int | None
    
class PostResponse(BaseModel):
    id: int
    text: str
    senderId: int
    create_date: str 
    senderEmail: str
    

class GetPostsResponseItem(BaseModel):
    id: int
    text: str
    senderId: int
    create_date: str | None
    images: list[str]
    senderUsername: str | None


class ReactPostRequest(BaseModel):
    postId: int
    like: bool
