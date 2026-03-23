from pydantic import BaseModel, Field


# Todo's id (or serial number) is not needed as its not user's headache.
class createTodo(BaseModel):
    todo_detail : str = Field(..., min_length=1, description="Todo's detail")

# Both id and detail needed as we're gonna use the id's as the key's for the checkbox and update/delete buttons, since streamlit throws error for similiar widgets.
# for now since we're not using the 'db', so we'll ignore the todo_id for now.
class responseTodo(BaseModel):
    id : int = Field(..., description="Todo's detail")
    todo_detail : str = Field(..., min_length=1, description="Todo's detail")

class updateTodo(createTodo):
    pass