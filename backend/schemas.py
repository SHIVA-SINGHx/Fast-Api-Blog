from pydantic import BaseModel

class BlogBase(BaseModel):
    name: str
    description: str
    author: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int

class BlogNoId(BlogBase):
    name:str
    description:str

    class Config:
        orm_mode = True 

class User(BaseModel):
    name: str
    email: str
    password: str