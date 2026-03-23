from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


import database
import app.todos.models
from app.todos.router import router as todos_router
from app.todos.models import Base


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Creating the tables (i.e models) - One time process.
Base.metadata.create_all(bind=database.engine)

# adding feature wise routers:
app.include_router(todos_router)


























# all_todos = {
#  1 :  {'id':1,'todo_detail': 'Hit arms'},                                        # todo_id will be taken care of by our db (using "index = True")
#  2 : {'id':2,'todo_detail': 'Finish shipping the todo feature'}
# }
