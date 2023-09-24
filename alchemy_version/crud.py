from models import eng, TodoLists, TodoItems
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=eng)
session = Session()

# CREATE


def create_todo_list(title):
    session.add(TodoLists(title=title))
    session.commit()


def create_task(list_id, name):
    session.add(TodoItems(name=name, list_id=list_id))
    session.commit()

# READ


def select_tasks():
    return session.query(TodoItems).all()


def select_task(id):
    return session.query(TodoItems).where(TodoItems.item_id == id).first()


""" Create two Functions to read all Lists and read one list by ID
Create Function to mark the task not complete
Crate delete Function to delete the todo list"""

# *** CREATE A SELECT TASK FOR TODO LISTS and LIST ***


def select_lists():
    return session.query(TodoLists).all()


def select_list(id):
    return session.query(TodoLists).where(TodoLists.list_id == id).first()

# UPDATE


def make_complete(id):
    task = select_task(id)
    task.state = True
    task.name = "asdasdasd"
    session.commit()

# *** CREATE UPDATE FUNC TO MAKE AS NOT COMPLETE ***


def update_task_not_complete(id):
    task = select_task(id)
    task.state = False
    session.commit()

# DELETE


def delete_task(id):
    task = select_task(id)
    session.delete(task)
    session.commit()

# CRATE A DELETE TASK FOR TODO LIST


def delete_todo_list(list_name):
    list = select_list(list_name)
    session.delete(list)
    session.commit()
