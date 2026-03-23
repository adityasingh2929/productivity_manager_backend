from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

load_dotenv()   # loads the env variables

url = os.getenv("DATABASE_URL")


   
engine = create_engine(url)
session = sessionmaker(autocommit=False, bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
    


