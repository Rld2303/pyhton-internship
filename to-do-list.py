tasks = []

while True:
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == "2":
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                print(f"Task '{deleted_task}' deleted.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to delete.")
    elif choice == "3":
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(tasks):
                completed_task = tasks.pop(task_index)
                print(f"Task '{completed_task}' marked as completed.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to mark as completed.")
    elif choice == "4":
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks.")
    elif choice == "5":
        print("Exiting Todo List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
