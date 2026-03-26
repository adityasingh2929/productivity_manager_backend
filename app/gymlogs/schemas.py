from pydantic import BaseModel, Field
from typing import Optional,List,Dict


class addLog(BaseModel):
    workout_type : str = Field(...,min_length=1, description="Workout type")
    workout_name : str = Field(...,min_length=1, description="Workout name")
    weight : float = Field(...,description="Amount of weight moved")
    reps : int = Field(...,description="Number of times weight moved")

class updateLog(BaseModel):
    workout_type : Optional[str] = Field(None,min_length=1, description="Workout type for updation")
    workout_name : Optional[str] = Field(None,min_length=7, description="Workout name for updation")
    weight : Optional[float] = Field(None,description="Amount of weight moved for updation")
    reps : Optional[int] = Field(None,min_length=1,description="Number of times weight moved for updation")

class responseLog(BaseModel):
    week_number : int = Field(..., description="Weekly session number")
    workout_name : str = Field(...,min_length=1, description="Workout name")
    weight : float = Field(...,description="Amount of weight moved")
    reps : int = Field(...,description="Number of times weight moved")

    class Config:
        from_attributes = True

    # since after fetching using sqlalchemy, it returns a list of ORM objects (not dicts), so this tells our schema to read from the orm objects and validate them and then fastapi converts them into dicts by:
    """
        obj = <Arms object>

        data = 
        {
            "id": obj.id,
            "weight": obj.weight,
            "reps": obj.reps,
            "session_n": obj.session_n
        }
    """


