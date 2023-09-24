import crud

# if __name__ == "__main__":
#     list_name = input("Enter the name of the list: ")
#     crud.create_todo_list(list_name)

#     task_title = input("Task title: ")
#     crud.create_task(1, task_title)

#     tasks = crud.select_tasks()
#     print(tasks[0].item_id)
#     one_task = crud.select_task(tasks[0].item_id)
#     crud.make_complete(one_task.item_id)

#     if one_task.state:
#         print("completed")
#     else:
#         print("not completed")

#     crud.delete_task(one_task.item_id)

# MAKE IT AN ACTUAL TODO APP


def main():
    while True:
        primary_action = input("1. Create a new list \n"
                               "2. Add a task to the list \n"
                               "3. Mark the task as completed or not \n"
                               "4. Look at all the lists \n"
                               "5. Delete a list \n"
                               "6. Look at all tasks assigned to the lists \n"
                               "7. Delete a task \n"
                               "8. Exit \n"
                               "Enter your choice: ")
# Create a new list and name the list
        if primary_action == "1":
            list_name = input("Enter the name of the list: ")
            crud.create_todo_list(list_name)
            print(f"{list_name} is created")
# Enter the task and add it to the list
        elif primary_action == "2":
            task_title = input("Enter the task title: ")
            crud.create_task(task_title)
            print(f"{task_title} is added to the list")
# Select a task and mark it as completed or not
        elif primary_action == "3":
            print(crud.select_lists())
            selected_list = input(
                "Select a list which tasks you want to mark: ")
            print(crud.select_tasks(selected_list))
            selected_task = input("Select a task which you want to mark: ")
            choice = input(
                "Enter 1 to mark the task as completed or 0 to mark it as not completed")
            if choice == "1":
                crud.make_complete(selected_task)
                print(f"{selected_task} is marked as completed")
            elif choice == "0":
                crud.make_not_complete(selected_task)
                print(f"{selected_task} is marked as not completed")
# Look at all the lists
        elif primary_action == "4":
            print(crud.select_lists())
# Delete a list
        elif primary_action == "5":
            return crud.delete_todo_list(input("Enter the name of the list you want to delete: "))
            print(f"{list_name} is deleted")
# Look at all the tasks assigned to the lists
        elif primary_action == "6":
            print(crud.select_lists())
# Delete a task
        elif primary_action == "7":
            return crud.delete_task(input("Enter the id of the task you want to delete: "))
            print(f"{task_title} is deleted")
# Exit the program
        elif primary_action == "8":
            break
        else:
            print("Something went wrong, please enter a valid choice")


if __name__ == "__main__":
    main()
