from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from Database.context import Base
import datetime

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    id_sender = Column(Integer,ForeignKey("users.id"))
    text = Column(String(200))
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    user = relationship("User", back_populates="posts")
    
class PostImage(Base):
    __tablename__ = "post_images"
    
    id = Column(Integer, primary_key=True)
    postId = Column(Integer,ForeignKey("posts.id"))
    imageAdress = Column(String(200))
    
    post = relationship("Post", back_populates="images")