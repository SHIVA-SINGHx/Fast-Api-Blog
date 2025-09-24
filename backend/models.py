from database import Base
from sqlalchemy import Column, String, Integer

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)
    author = Column(String, index=True)


class User(Base):
    __tablename__ = "users"
    
    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String, index=True)
    email= Column(String, index=True)
    password= Column(String, index=True)