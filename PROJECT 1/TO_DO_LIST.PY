task =[]

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter a choice (1-5): ")

    # ADD TASK
    if choice == "1":
        task_name = input("Enter task: ")
        new_task = {"task": task_name, "done": False}
        task.append(new_task)
        print("Task added!")

    # VIEW TASK
    elif choice == "2":
        if not task:
            print("No tasks yet")
        else:
            for index, t in enumerate(task, 1):
                print(index, t["task"], "- Completed:", t["done"])

    # MARK COMPLETE
    elif choice == "3":
        if not task:
            print("No tasks available")
        else:
            for index, t in enumerate(task, 1):
                print(index, t["task"])

            num = int(input("Enter task number to mark complete: "))

            if 1 <= num <= len(task):
                task[num - 1]["done"] = True
                print("Marked as complete!")
            else:
                print("Invalid task number")

    # DELETE TASK
    elif choice == "4":
        if not task:
            print("No tasks available")
        else:
            for index, t in enumerate(task, 1):
                print(index, t["task"])

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(task):
                task.pop(num - 1)
                print("Task deleted!")
            else:
                print("Invalid task number")

    # EXIT
    elif choice == "5":
        print("Exiting To-Do List")
        break

    else:
        print("Invalid choice")