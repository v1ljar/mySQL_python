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

# UPDATE


def make_complete(id):
    task = select_task(id)
    task.state = True
    task.name = "asdasdasd"
    session.commit()

# DELETE


def delete_task(id):
    task = select_task(id)
    session.delete(task)
    session.commit()
