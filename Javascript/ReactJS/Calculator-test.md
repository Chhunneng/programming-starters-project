# React Calculator

A simple calculator built with React that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The calculator has an intuitive user interface, making it easy to use for anyone.

## Features

- **Basic Operations**: Supports addition, subtraction, multiplication, and division.
- **Clear Functionality**: Reset the input and result with a clear button.
- **Error Handling**: Displays an error message for invalid expressions.
- **Responsive Design**: Adapts to different screen sizes with a simple layout.
- **Read-only Input Field**: The input field is read-only to prevent manual editing while performing calculations.




## Main Code

### Calculator Component (App.jsx)

```jsx
import { useEffect, useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const buttons = ["C", 0, "=", "/", 1, 2, 3, "*", 4, 5, 6, "-", 7, 8, 9, "+"];
  const [result, setResult] = useState("");

  const handleClick = (value) => {
    setInput((prev) => prev + value);
  };

  const handleClear = () => {
    setInput("");
    setResult("");
  };

  const handleChange = (e) => {
    setInput(e.target.value);
  };

  const handleEvaluate = () => {
    if (
      input === "" ||
      /[+\-*/]$/.test(input.charAt(input.length - 1)) ||
      input.length <= 2
    ) {
      console.log(input.length);
      setResult("Error");
    } else {
      let out = eval(input);
      setResult(out);
      setInput("");
    }
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <h1>React Calculator</h1>
      <input
        readOnly
        type="text"
        name=""
        value={input}
        onChange={handleChange}
      />
      <div>{result}</div>

      <div
        className="buttons"
        style={{
          width: "300px",
          display: "flex",
          gap: "10px",
          padding: "20px",
          justifyContent: "center",
          alignItems: "center",
          flexWrap: "wrap-reverse",
        }}
      >
        {buttons.map((button) => (
          <button
            key={button}
            style={{
              height: "60px",
              width: "60px",
              borderRadius: "10px",
              fontSize: "30px",
            }}
            onClick={
              button === "C"
                ? handleClear
                : button === "="
                ? handleEvaluate
                : () => handleClick(button)
            }
          >
            {button}
          </button>
        ))}
      </div>
    </div>
  );
}

export default App;
```

And the main.jsx file which will inject the code in the DOM

```jsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```
