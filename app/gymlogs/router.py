from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from pydantic import BaseModel


import database
from . import models
from . import schemas

gym_router = APIRouter(prefix="/gym",tags=["Gym"])


@gym_router.post("/weeks")
def create_gym_week(db : Session = Depends(database.get_db)):
    new_week = models.gymWeek()
    db.add(new_week)
    db.commit()
    db.refresh(new_week)
    return new_week

@gym_router.get("/weeks", response_model=List[schemas.gymWeekResponse])
def fetch_gym_week(db : Session = Depends(database.get_db)):
    fetch = db.query(models.gymWeek).all()               # we use the model's class not the tablename here, in order to validate/fetch the data as per the db format.
    if fetch:
        return fetch
    raise HTTPException(status_code=404, detail=f"{fetch}")

@gym_router.get("/weeks/logs", response_model=List[schemas.responseLog])
def fetch_logs(week_number : int, workout_name : str, db : Session = Depends(database.get_db)):
    week_check = db.query(models.gymWeek).filter(models.gymWeek.week_number == week_number).first()
    if week_check:
        logs = db.query(models.WorkoutLogs).filter(models.WorkoutLogs.week_number == week_number, models.WorkoutLogs.workout_name == workout_name).order_by(models.WorkoutLogs.set).all()
        if logs:
            return logs
        raise HTTPException(status_code=404, detail="Logs not found")
    raise HTTPException(status_code=404, detail="Week not found")

@gym_router.post("/weeks/logs", response_model=schemas.responseLog)
def add_logs(week_number : int, payload : schemas.addLog, db : Session = Depends(database.get_db)):  # workout_n,weight,reps are grouped into an object called 'payload'
    week_check = db.query(models.gymWeek).filter(models.gymWeek.week_number == week_number).first()
    if week_check:
        log = payload.model_dump()
        log["week_number"] = week_number

        added_log = models.WorkoutLogs(**log)
        db.add(added_log)
        db.commit()
        db.refresh(added_log)
        return added_log
    raise HTTPException(status_code=404, detail="Week not found")

@gym_router.put("/weeks/logs", response_model=schemas.responseLog)
def update_logs(id : int, payload : schemas.updateLog, db : Session = Depends(database.get_db)):
    log = db.query(models.WorkoutLogs).filter(models.WorkoutLogs.id == id).first()
    if log:
        if payload.workout_name is not None:
            log.workout_name = payload.workout_name
        if payload.workout_type is not None:
            log.workout_type = payload.workout_type
        if payload.weight is not None:
            log.weight = payload.weight
        if payload.reps is not None:
            log.reps = payload.reps
        db.commit()
        db.refresh(log)
        return log
    raise HTTPException(status_code=404, detail="Log not found")

@gym_router.delete("/weeks/logs", response_model=schemas.responseLog)
def delete_logs(id : int, db : Session = Depends(database.get_db)):
    log = db.query(models.WorkoutLogs).filter(models.WorkoutLogs.id == id).first()
    if log:
        temp = log
        db.delete(log)
        db.commit()
        return temp
    raise HTTPException(status_code=404, detail="Log not found") 


@gym_router.get("/getall", response_model=List[schemas.responseLog])
def fetch_all(week_number : int, db : Session = Depends(database.get_db)):
    week_check = db.query(models.gymWeek).filter(models.gymWeek.week_number == week_number).first()
    if week_check:
        logs = db.query(models.WorkoutLogs).all()
        return logs
    raise HTTPException(status_code=404, detail="Logs not found")
