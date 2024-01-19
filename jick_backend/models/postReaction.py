from Database.context import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime,Boolean
import datetime

class postReaction(Base):
    __tablename__ = "postReactions"
    
    id = Column(Integer, primary_key=True)
    postId = Column(Integer)
    userId = Column(Integer)
    can_like = Column(Boolean)
    
    def __init__(self, postId, userId, can_like : bool):
        self.postId = postId
        self.userId = userId
        self.can_like = can_like
        
    def __repr__(self):
        return "<postReaction(postId='%s', userId='%s', reaction='%b')>" % (
            self.postId, self.userId, self.can_like)