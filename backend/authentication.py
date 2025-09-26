from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database import get_db
import models, schemas

app = FastAPI()

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# LOGIN FUNCTION
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return False
    
    if not pwd_cxt.verify(password, user.password):
        return False
    
    return user

