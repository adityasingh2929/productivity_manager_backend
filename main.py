from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware


import database
# import app.todos.models
# from app.todos.router import todos_router
from app.gymlogs.router import gymlogs_router
# from app.todos.models import BaseT
from app.gymlogs.models import BaseG



app = FastAPI()

#uncomment this, todos_api.py and 1 todos.py
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], 
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# Creating the tables (i.e models) - One time process.
# BaseT.metadata.create_all(bind=database.engine)
BaseG.metadata.create_all(bind=database.engine)

# adding feature wise routers:
# app.include_router(todos_router)
app.include_router(gymlogs_router)


























# all_todos = {
#  1 :  {'id':1,'todo_detail': 'Hit arms'},                                        # todo_id will be taken care of by our db (using "index = True")
#  2 : {'id':2,'todo_detail': 'Finish shipping the todo feature'}
# }
