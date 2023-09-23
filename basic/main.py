from mysql.connector import connect, Error
from crud import 

create_database_query = "CREATE DATABASE IF NOT EXISTS todo_app"

try:
    with connect(host="localhost", user="admin", password="root", port="3307", database="todo_app") as conn:
        with conn.cursor() as cursor:
            cursor.excecute(create_database_query)

except Error as e:
    print(e)
