# Todo App in ReactJS

Welcome to the Todo App project for ReactJS! ⚛️

In this project, we'll create a todo list web application using ReactJS. Let's get started!

## Project Overview

### Objective

Create a ReactJS application that functions as a todo list.

### Features

- Add new todo items.
- Mark items as completed.
- Delete todo items.
- Filter items by all, active, and completed.

## Project Structure

Create a new ReactJS project using your preferred setup (e.g., Create React App) and organize the components accordingly.

## Instructions

1. **Set Up React App:**
   - Create a new ReactJS app using a tool like Create React App.
   - Set up the project structure and create necessary components.

2. **Todo Interface:**
   - Design an interface with an input field for adding new todo items and a list to display the todos.

3. **State Management:**
   - Manage the state of the todos to keep track of the list of items, their completion status, and current filter.

4. **Add Todo Item:**
   - Implement functionality to add new items to the todo list.

5. **Mark as Completed:**
   - Implement functionality to mark items as completed.

6. **Delete Todo Item:**
   - Implement functionality to delete items from the todo list.

7. **Filter Items:**
   - Implement functionality to filter items by all, active, and completed.

8. **Run the App:**
   - Start the development server and open the app in a web browser.

## Example Code

### Calculator Component (Calculator.js)

```jsx
import React, { useState } from 'react';

const TodoApp = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');
  const [filter, setFilter] = useState('all');

  const handleAddTodo = () => {
    if (newTodo.trim() !== '') {
      setTodos([...todos, { text: newTodo, completed: false }]);
      setNewTodo('');
    }
  };

  const handleToggleComplete = (index) => {
    const updatedTodos = todos.map((todo, i) =>
      i === index ? { ...todo, completed: !todo.completed } : todo
    );
    setTodos(updatedTodos);
  };

  const handleDeleteTodo = (index) => {
    const updatedTodos = todos.filter((_, i) => i !== index);
    setTodos(updatedTodos);
  };

  const handleFilterChange = (newFilter) => {
    setFilter(newFilter);
  };

  const filteredTodos = todos.filter((todo) => {
    if (filter === 'all') return true;
    if (filter === 'active') return !todo.completed;
    if (filter === 'completed') return todo.completed;
    return true;
  });

  return (
    <div>
      <h1>Todo App</h1>
      <input
        type="text"
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
        placeholder="Add a new todo"
      />
      <button onClick={handleAddTodo}>Add</button>
      <div>
        <button onClick={() => handleFilterChange('all')}>All</button>
        <button onClick={() => handleFilterChange('active')}>Active</button>
        <button onClick={() => handleFilterChange('completed')}>Completed</button>
      </div>
      <ul>
        {filteredTodos.map((todo, index) => (
          <li key={index}>
            <span
              style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
              onClick={() => handleToggleComplete(index)}
            >
              {todo.text}
            </span>
            <button onClick={() => handleDeleteTodo(index)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoApp;
```

Remember to customize the todo app, add features, or modify the structure as you see fit. Contributors can use this document as a guide to implementing the todo app in ReactJS.