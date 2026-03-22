from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


url = "postgresql://postgres:password@localhost:5432/productivity_management"    
engine = create_engine(url)
session = sessionmaker(autocommit=False, bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
    


