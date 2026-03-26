from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Float, Column, Integer, String

BaseT = declarative_base()

class Todos(BaseT):

    __tablename__ = "Todos"

    id = Column(Integer, primary_key=True, index=True)
    todo_detail = Column(String)
