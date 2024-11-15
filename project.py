# project.py

def main():
    print("Welcome to the To-Do List Manager!")
    # You could add a simple menu here to let users choose actions
    while True:
        action = input("Choose an action: add, view, remove, or quit: ").strip().lower()
        if action == "add":
            add_task()
        elif action == "view":
            view_tasks()
        elif action == "remove":
            remove_task()
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please try again.")

tasks = []  # Global list to store tasks

def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
