from mysql.connector import connect, Error
from crud import create_database_query, create_tables_query, add_todo_list_query, create_item_to_list, select_all_tasks_query, delete_item_from_list


def setup_db():
    try:
        with connect(host="localhost", user="admin", password="admin", port="3307") as conn:
            with conn.cursor() as cursor:
                cursor.execute(create_database_query)
                cursor.execute("USE todo_app")
                cursor.execute(create_tables_query)

    except Error as e:
        print(e)


def create_todo_list(title):
    try:
        with connect(host="localhost", user="admin", password="admin", port="3307", database="todo_app") as conn:
            with conn.cursor() as cursor:
                cursor.execute(add_todo_list_query(title))
                conn.commit()
    except Error as e:
        print(e)


def create_task(list_id, name):
    try:
        with connect(host="localhost", user="admin", password="admin", port="3307", database="todo_app") as conn:
            with conn.cursor() as cursor:
                # Check if the list_id exists in the todo_lists table
                cursor.execute(
                    "SELECT 1 FROM todo_lists WHERE list_id = %s", (list_id,))
                if cursor.fetchone():
                    cursor.execute(create_item_to_list(list_id, name))
                    conn.commit()
                else:
                    print(f"List with list_id {list_id} does not exist.")
    except Error as e:
        print(e)


def select_tasks():
    try:
        with connect(host="localhost", user="admin", password="admin", port="3307", database="todo_app") as conn:
            with conn.cursor() as cursor:
                cursor.execute(select_all_tasks_query)
                print(cursor.fetchone())
                print("pajspdjpij")
                print(cursor.fetchall())

    except Error as e:
        print(e)


def delete_task(task_id):
    try:
        with connect(host="localhost", user="admin", password="admin", port="3307", database="todo_app") as conn:
            with conn.cursor() as cursor:
                cursor.execute(delete_task_query(task_id))
                conn.commit()
    except Error as e:
        print(e)


if __name__ == "__main__":
    setup_db()
    # list_name = input("Enter the name of the list: ")
    # create_todo_list(list_name)

    # task_title = input("Task title: ")
    create_task(1, task_title)
    delete_task(5)
    select_tasks()
