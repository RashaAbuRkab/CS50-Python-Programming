import sys

def main():
    print(welcome())
    Task = {}
    complete = {}

    while True:
        num = input("Enter your choice: ")
        if num == '1':
            # Gather inputs for adding a task
            task = input("Enter Your Task: ")
            task_id = input("Task ID (Just Integer Number): ")
            Task = add_task(Task, task, task_id)  # Pass all required arguments
        elif num == '2':
            complete_id = input("Enter Task ID: ")
            completed(Task, complete, complete_id)
        elif num == '3':
            delete_id = input("Enter Task ID to Delete: ")
            del_task(Task, delete_id)
        elif num == '4':
            print_completed(complete)
        elif num == '5':
            print_all(Task)
        elif num == '6':
            sys.exit("Goodbye")
        else:
            print("Invalid Number")

def welcome():
    return """
        <============ Task Manager 📝 ============>
            Welcome To Our Task Manager
        What would you do :
        1. Add Task ✒️
        2. Mark Task As Completed 👏
        3. Delete Task ❌
        4. Show your Completed Task ✔️
        5. Print All In-Progress Tasks ⏳
        6. Exit 👋
        <============ Task Manager 📝 ============>
    """

def add_task(Task, task, task_id):
    Task[task_id] = task
    return Task

def del_task(Task, task_id):
    if task_id in Task.keys():
        del Task[task_id]
        return True
    return False

def completed(Task, complete, complete_id):
    if complete_id in Task.keys():
        complete[complete_id] = Task[complete_id]
        del Task[complete_id]
        return True
    return False

def print_completed(complete):
    return [f'{complete[item]} With ID: {item} Completed ✔️' for item in complete.keys()]

def print_all(Task):
    return [f'{Task[item]} With ID: {item} In Progress 🕜' for item in Task.keys()]

if __name__ == "__main__":
    main()
