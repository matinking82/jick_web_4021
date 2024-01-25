from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from Database.context import Base
import datetime

class admin(Base):
    __tablename__ = "admin"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(200))
    password = Column(String(200))
    
    
