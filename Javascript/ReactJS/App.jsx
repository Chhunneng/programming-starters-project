import { useEffect, useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const buttons = ["C", 0, "=", "/", 1, 2, 3, "*", 4, 5, 6, "-", 7, 8, 9, "+"];
  const [result, setResult] = useState("");

  const handleClick = (value) => {
    // console.log(value)
    setInput((prev) => prev + value);
  };

  const handleClear = () => {
    // console.log("cleared");
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
