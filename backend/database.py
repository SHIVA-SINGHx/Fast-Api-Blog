from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Connecting database with postgresql

db_url = "postgresql+psycopg2://postgres:Adminshiva123@localhost:5432/fastapi-blog"
engine = create_engine(db_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db():
    Base.metadata.create_all(bind=engine)