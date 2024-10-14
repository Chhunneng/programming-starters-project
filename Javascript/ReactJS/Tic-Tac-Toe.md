# Tic-Tac-Toe in ReactJS

Welcome to the Tic-Tac-Toe project for ReactJS! ⚛️

In this project, we'll create a tic-tac-toe web application using ReactJS. Let's get started!

## Project Overview

### Objective

Create a ReactJS application that functions as a tic-tac-toe game.

### Features

- Interactive tic-tac-toe game board.
- Player turn management (X and O).
- Win condition checking.
- Game reset functionality.

## Project Structure

Create a new ReactJS project using your preferred setup (e.g., Create React App) and organize the components accordingly.

## Instructions

1. **Set Up React App:**
   - Create a new ReactJS app using a tool like Create React App.
   - Set up the project structure and create necessary components.

2. **Game Interface:**
   - Design an interface with a 3x3 grid for the game board and display the current player's turn and winner.

3. **State Management:**
   - Manage the state of the game board to keep track of the current player's moves and the game status.

4. **Render Squares:**
   - Implement functionality to render squares and handle player clicks on the board.

5. **Check Winner:**
   - Implement functionality to check for a winner after each move.

6. **Reset Game:**
   - Implement functionality to reset the game when it's over or when the reset button is clicked.

7. **Run the App:**
   - Start the development server and open the app in a web browser.

## Example Code

### App Component (App.js)

```jsx
import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [isXNext, setIsXNext] = useState(true);
  const winner = calculateWinner(board);

  const handleClick = (index) => {
    if (board[index] || winner) return; // Ignore if square is already filled or if there's a winner
    const newBoard = board.slice();
    newBoard[index] = isXNext ? 'X' : 'O';
    setBoard(newBoard);
    setIsXNext(!isXNext);
  };

  const renderSquare = (index) => {
    return (
      <button className="square" onClick={() => handleClick(index)}>
        {board[index]}
      </button>
    );
  };

  const resetGame = () => {
    setBoard(Array(9).fill(null));
    setIsXNext(true);
  };

  return (
    <div className="game">
      <h1>Tic-Tac-Toe</h1>
      <div className="status">
        {winner ? `Winner: ${winner}` : `Next player: ${isXNext ? 'X' : 'O'}`}
      </div>
      <div className="board">
        <div className="board-row">
          {renderSquare(0)}
          {renderSquare(1)}
          {renderSquare(2)}
        </div>
        <div className="board-row">
          {renderSquare(3)}
          {renderSquare(4)}
          {renderSquare(5)}
        </div>
        <div className="board-row">
          {renderSquare(6)}
          {renderSquare(7)}
          {renderSquare(8)}
        </div>
      </div>
      <button className="reset" onClick={resetGame}>
        Reset Game
      </button>
    </div>
  );
};

// Helper function to check for a winner
const calculateWinner = (squares) => {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
};

export default App;
```


Remember to customize the todo app, add features, or modify the structure as you see fit. Contributors can use this document as a guide to implementing the todo app in ReactJS.
