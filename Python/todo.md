# To-Do List Application

This is a simple To-Do List application built using Python's Tkinter library. It allows users to add and delete tasks from a list. 

## Features

- Add tasks to your to-do list.
- Delete selected tasks from the list.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository or download the files to your local machine.

3. Navigate to the project directory in your terminal.

## Usage

Run the application by executing the following command:

```bash
python todo_list.py
```

## CODE
Below is the code for the To-Do List application:

```python

import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
```
Feel free to enhance the Todo list, add features, or modify the structure as you see fit. Contributors can use this document as a guide to implementing the Todo list in Python.

