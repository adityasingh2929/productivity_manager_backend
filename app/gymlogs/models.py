from sqlalchemy import String, Column, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

BaseG = declarative_base()

class gymWeek(BaseG):
    __tablename__ = "gymweek"

    week_number = Column(Integer,primary_key=True)

class WorkoutLogs(BaseG):

    __tablename__ = "workoutlogs"

    id = Column(Integer,primary_key=True)
    week_number = Column(Integer, ForeignKey("gymweek.week_number"))         # SQLAlchemy uses a table name for assigning foreign key, not the classname (gymWeek)
    workout_type = Column(String)
    workout_name = Column(String)
    weight = Column(Float)
    reps = Column(Integer)
    set = Column(Integer)
