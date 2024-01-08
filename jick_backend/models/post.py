from sqlalchemy import Column, ForeignKey, Integer, String, DateTime,BLOB
from sqlalchemy.orm import relationship
from Database.context import Base
import datetime

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    id_sender = Column(Integer,ForeignKey("users.id"))
    text = Column(String(200))
    image = Column(BLOB)
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    user = relationship("User", back_populates="posts")
    
