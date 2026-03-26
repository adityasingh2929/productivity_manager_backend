from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from pydantic import BaseModel


import database
from . import models
from . import schemas




gymlogs_router = APIRouter(prefix="/gymlogs",tags=["gymlogs"])


@gymlogs_router.get("/", response_model=List[schemas.responseLog])
def fetch_logs(session_n : int, db : Session = Depends(database.get_db)):
    pass

@gymlogs_router.post("/")
def create_gym_week():
    pass

@gymlogs_router.post("/", response_model=schemas.responseLog)
def add_logs(table_n : str, payload : schemas.addLog, db : Session = Depends(database.get_db)):  # workout_n,weight,reps are grouped into an object called 'payload'
    pass

@gymlogs_router.put("/", response_model=schemas.responseLog)
def update_logs(table_n : str, workout_n : str, session_n : int, payload : schemas.updateLog, db : Session = Depends(database.get_db)):
    pass


@gymlogs_router.delete("/", response_model=schemas.responseLog)
def delete_logs(table_n : str, session_n : int, workout_n : str, db : Session = Depends(database.get_db)):
    pass



