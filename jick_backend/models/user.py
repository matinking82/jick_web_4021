from sqlalchemy import Column, Integer, String, Boolean, DateTime
from Database.context import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    is_active = Column(Boolean, default=False)
    guid_token = Column(String(100), unique=True)
    password = Column(String(100))
    full_name = Column(String(100))
    age = Column(Integer)
    create_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

