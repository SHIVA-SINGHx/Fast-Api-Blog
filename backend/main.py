from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, blog, authentication
from database import engine, Base, get_db


app = FastAPI()

Base.metadata.create_all(bind=engine)


# create blog 
@app.post("/blog", response_model=schemas.Blog)
def create_blog_route(blog_data: schemas.BlogCreate, db: Session = Depends(get_db)):
    return blog.create_blog(db, blog_data)

# get blog
@app.get("/blog", response_model= list[schemas.Blog])
def get_blog(db: Session= Depends(get_db)):
    return blog.get_blog(db)

# get blog by {id}
@app.get("/blog/{id}", response_model= schemas.Blog)
def get_one_blog(id:int, db: Session = Depends(get_db)):
    product_query = blog.get_blog_id(db,id)
    if product_query:
        return product_query
    
    raise HTTPException(status_code= 404, detail= "Cannot find the id")

# update blog
@app.put("/blog/{id}", response_model = schemas.Blog)
def update_blog(id: int, product: schemas.BlogCreate, db: Session = Depends(get_db)):
    db_update = blog.update_blog(db,product,id)
    if db_update:
        return db_update
    raise HTTPException(status_code=404, detail= "Invalid Update id")

# delete blog
@app.delete("/blog/{id}", response_model = schemas.Blog)
def delete_blog(id:int, db:Session = Depends(get_db)):
    blog_delete = blog.delete_blog(db, id)
    if blog_delete:
        return blog_delete
    
    raise HTTPException(status_code=404, detail="Blog not found")

# CREATED USER ROUTES

@app.post("/user/", response_model=schemas.ShowUser)
def create_user(data: schemas.UserCreate, db: Session = Depends(get_db)):
    return blog.create_user(db, data)


# Get user by ID
@app.get("/user/{id}", response_model=schemas.ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user_query = blog.get_user(db, id)
    if not user_query:
        raise HTTPException(status_code=404, detail="Invalid User ID")
    return user_query


 # LOGIN ROUTES
 
@app.post("/login", response_model= schemas.Login)
def login_user(login_data: schemas.Login, db: Session= Depends(get_db)):
    user = 