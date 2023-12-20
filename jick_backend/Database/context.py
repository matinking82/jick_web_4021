from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Boolean,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os,datetime

Base = declarative_base()


# Create your models here.
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




# database connection
DATABASE_URL = os.environ["DBUrl"]  # Use an appropriate database URL
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()