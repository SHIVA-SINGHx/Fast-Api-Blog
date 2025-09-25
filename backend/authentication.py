from fastapi import FastAPI
from sqlalchemy.orm import Session
from schemas import Login
from passlib.context import CryptContext
import database

app = FastAPI()

def login(db: Session, data:Login):
    login_instance = Login(**data.model_dump())
    db.add(login_instance)
    db.commmit()
    db.refresh(login_instance)
    
    return login
