# Simple Command-Line To-Do List Application in Python

todo_list = []
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")
def list_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")
def complete_task(task_index):
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(todo_list):
            completed_task = todo_list.pop(task_index - 1)
            print(f"Task '{completed_task}' marked as completed.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid task index.")
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_index = input("Enter the task index to mark as completed: ")
            complete_task(task_index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
