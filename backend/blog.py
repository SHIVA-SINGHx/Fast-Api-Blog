from sqlalchemy.orm import Session
from models import Blog
from schemas import BlogCreate


def create_blog(db: Session, data: BlogCreate):
    blog_instance = Blog(**data.model_dump())
    db.add(blog_instance)
    db.commit()
    db.refresh(blog_instance)
    return blog_instance

def get_blog(db:Session):
    return db.query(Blog).all()

def get_blog_id(db: Session, blog_id: int):
     return db.query(Blog).filter(Blog.id == blog_id).first()
    

