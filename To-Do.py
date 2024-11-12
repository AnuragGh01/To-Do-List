todo_list = []

# Add a task
def add_task(task):
    todo_list.append(task)
    print(f"Added task: {task}")

# View all tasks
def view_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("Your To-Do List:")
        for task in todo_list:
            print(f"- {task}")

# Remove a task
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Removed task: {task}")
    else:
        print(f"Task '{task}' not found.")

# Main program loop
while True:
    print("\n1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Choose an option (1-4) or type 'exit' to quit: ").lower()

    if choice == '1':
        view_tasks()
    elif choice == '2':
        task = input("Enter a task (or type 'exit' to quit): ")
        if task.lower() == 'exit':
            print("Goodbye!")
            break
        add_task(task)
    elif choice == '3':
        task = input("Enter the task to remove (or type 'exit' to quit): ")
        if task.lower() == 'exit':
            print("Goodbye!")
            break
        remove_task(task)
    elif choice == '4' or choice == 'exit':
        print("Goodbye!")
        break
    elif choice == 'exit':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
