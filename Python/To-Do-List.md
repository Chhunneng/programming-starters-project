# 📝 To-Do List App in Python

Welcome to the **To-Do List App** project for Python! 🐍  

In this project, we'll create a **command-line To-Do List** where users can **add, view, complete, and delete tasks**.  
This is a great beginner project for practicing **Python file handling, lists, functions, and user input**.

---

## Project Overview

### Objective
Create a Python script that implements a simple **To-Do List application** in the command line.

### Features
- ✅ Add new tasks to the list  
- ✅ View all tasks (pending and completed)  
- ✅ Mark tasks as complete  
- ✅ Delete tasks  
- ✅ Save tasks to a file and load them on program start  

### Project Structure
Create a new Python script named `todo_list.py`.

---

## Instructions

1. **Load Tasks from File**  
   - At the start, read tasks from a file (if it exists) to maintain persistence.

2. **Display Menu**  
   - Show options like: `Add Task`, `View Tasks`, `Complete Task`, `Delete Task`, `Exit`.

3. **Add a Task**  
   - Prompt the user to enter a task description.  
   - Save it to the tasks list.

4. **View Tasks**  
   - Display all tasks with numbering.  
   - Optionally indicate which tasks are completed.

5. **Complete a Task**  
   - Ask the user for the task number to mark as complete.  
   - Update the status in the list.

6. **Delete a Task**  
   - Ask the user for the task number to delete.  
   - Remove it from the list.

7. **Save Tasks to File**  
   - After each modification, save the current tasks list to a file for persistence.

8. **Exit Program**  
   - End the program when the user chooses to exit.

---

## Example Code

```python
import os

# File to store tasks
TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                description, status = line.strip().split("|")
                tasks.append({"description": description, "completed": status=="True"})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(f"{task['description']}|{task['completed']}\n")

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. [{status}] {task['description']}")

# Add a new task
def add_task(tasks):
    description = input("Enter the task description: ")
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")

# Complete a task
def complete_task(tasks):
    view_tasks(tasks)
    number = int(input("Enter the task number to mark as complete: "))
    if 0 < number <= len(tasks):
        tasks[number-1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    number = int(input("Enter the task number to delete: "))
    if 0 < number <= len(tasks):
        removed = tasks.pop(number-1)
        save_tasks(tasks)
        print(f"Task '{removed['description']}' deleted successfully.")
    else:
        print("Invalid task number.")

# Main program
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

## Code Explanation

1️⃣ File Handling
Load tasks from a file at the start to maintain persistence.
Save tasks after every modification (add, complete, delete).

2️⃣ Task Management
Tasks are stored as dictionaries with description and completed status.
Functions like add_task, complete_task, delete_task, and view_tasks handle all operations.

3️⃣ Menu System
A loop displays options to the user.
User input directs to the corresponding function.
Program continues until the user selects Exit.

4️⃣ Task Status
✓ indicates completed tasks
✗ indicates pending tasks

## Example Output
--- To-Do List Menu ---
1. View Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Exit
Enter your choice: 2
Enter the task description: Finish Hacktoberfest PR
Task added successfully.

--- To-Do List Menu ---
1. View Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Exit
Enter your choice: 1
1. [✗] Finish Hacktoberfest PR

## 🛠 To-Do List for Contributors
- [ ] Add input validation for task numbers and menu choices
- [ ] Implement sorting tasks by status or alphabetically
- [ ] Add due dates for tasks and reminders
- [ ] Add option to edit existing tasks
- [ ] Add search functionality for tasks
- [ ] Improve menu display with colors or formatting

