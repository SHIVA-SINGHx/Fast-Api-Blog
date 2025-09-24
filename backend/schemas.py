from pydantic import BaseModel

class BlogBase(BaseModel):
    name: str
    description: str
    author: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int

    class Config:
        orm_mode = True 
