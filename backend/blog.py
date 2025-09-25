from sqlalchemy.orm import Session
from models import Blog, User
from schemas import BlogCreate, UserCreate
from passlib.context import CryptContext




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

def update_blog(db: Session, blog:BlogCreate, blog_id: int):
    blog_query = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog_query:
        for key, value in blog.dict().items():
            setattr(blog_query, key, value)
            
            db.commit()
            db.refresh(blog_query)
            return blog_query

def delete_blog(db: Session, id: int):
    blog_query = db.query(Blog).filter(Blog.id == id).first()
    if blog_query:
        db.delete(blog_query)
        db.commit()
        return blog_query


#Hash password
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User Section
def create_user(db: Session, data: UserCreate):
    
    hashed_password = pwd_cxt.hash(data.password)

    user_data = data.model_dump()
    user_data["password"] = hashed_password  

    user_instance = User(**user_data)   
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)
    return user_instance