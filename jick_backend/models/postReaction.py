from Database.context import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime,Boolean
import datetime

class postReaction(Base):
    __tablename__ = "postReactions"
    
    id = Column(Integer, primary_key=True)
    postId = Column(Integer)
    userId = Column(Integer)
    like = Column(Boolean)
    
    def __init__(self, postId, userId, like : bool):
        self.postId = postId
        self.userId = userId
        self.like = like
        
    def __repr__(self):
        return "<postReaction(postId='%s', userId='%s', reaction='%b')>" % (
            self.postId, self.userId, self.like)