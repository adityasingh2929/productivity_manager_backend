from typing import List, Dict
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models as models
from . import schemas as schemas
import database



todos_router = APIRouter(prefix="/todos", tags=["todos"])

# FETCHING TODOs
@todos_router.get('/', response_model=List[schemas.responseTodo])   
def get_todos(db : Session = Depends(database.get_db)):     # the 'db' is used to create a session with the database in order to perform crud operations.

    fetched_data = db.query(models.Todos).order_by(models.Todos.id).all()
    if fetched_data:
        return fetched_data
    raise HTTPException(status_code=404,detail="Todos not Found")


# CREATING TODOs
@todos_router.post('/', response_model=schemas.responseTodo)
def create_todo(todo_input : schemas.createTodo, db : Session = Depends(database.get_db)):

    # Generating todo_id:
    maximum = db.query(func.max(models.Todos.id)).scalar() 
    generated_todo_id = (maximum or 0) + 1              # instead of 'maximum+1' we did this because what if the table's empty, in that case there's no maximum, hence we just wouldnt have been able to create a todo in that case.

    new_todo = {'id': generated_todo_id, 'todo_detail': todo_input.todo_detail}

    db.add(models.Todos(**new_todo))
    db.commit()

    return new_todo
    


# UPDATING TODOs
@todos_router.put('/', response_model=schemas.responseTodo)
def update_todo(todo_id:int,todo_update : schemas.updateTodo, db : Session = Depends(database.get_db)):
    target_todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if target_todo:
        if(len(todo_update.todo_detail)>0):
            target_todo.todo_detail = todo_update.todo_detail
        db.commit()
        return target_todo
    
    raise HTTPException(status_code=404,detail="Todo not found")


# DELETING TODOs
@todos_router.delete('/',response_model=schemas.responseTodo)
def delete_todo(todo_id: int, db : Session = Depends(database.get_db)):
    
    target_todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if target_todo:
        temp = target_todo
        db.delete(target_todo)
        db.commit()
        return temp
    raise HTTPException(status_code=404, detail="Todo not found")



















# Inserting some values in the table at the start:  We'll have to make sure that this only occurs once.
# def init_db():
#     db = database.session()
#     count = db.query(models.Todos).count()
#     if count==0:
#         todos = list(all_todos.values())
#         for todo in todos:
#             processed_todo = models.Todos(**(todo))
#             db.add(processed_todo)
#         db.commit() # after committing, the session will get closed hence done at the end.

# init_db()