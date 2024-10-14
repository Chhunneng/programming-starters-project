# Random Joke Generator

Welcome to the Random Joke Generator, a fun web app that fetches and displays hilarious jokes to brighten your day!

## Project Overview

### Objective
Create a JavaScript script that fetches and displays random jokes from an API.

### Features
- Fetch random jokes from a public API.
- Display the jokes dynamically on a web page.
- Allow users to fetch a new random joke by clicking a button.

## Project Structure
Create a new HTML file named `index.html` and a JavaScript file named `random_joke_generator.js`.

## Instructions

### 1. Set Up HTML Structure
Create an HTML file with a basic structure, including an area to display the random joke and a button to fetch a new one.

### 2. Fetch Jokes from API
Use JavaScript to fetch random jokes from a public API (e.g., Official Joke API).

### 3. Display Jokes Dynamically
Update the HTML content dynamically to display the fetched jokes.

### 4. Handle Button Click
Add functionality to allow users to click a button to fetch a new random joke without refreshing the page.

### 5. Run the Script
Open the HTML file in a web browser to see the random jokes in action.

## Example Code

### HTML (`index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Random Joke Generator</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background-color: #f4f4f4;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }

    #joke-container {
      text-align: center;
      padding: 20px;
      background-color: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #joke-setup {
      font-size: 1.5rem;
      margin-bottom: 10px;
    }

    #joke-punchline {
      font-style: italic;
      color: #555;
      margin-bottom: 15px;
    }

    #new-joke-btn {
      background-color: #007bff;
      color: #fff;
      border: none;
      padding: 10px 20px;
      font-size: 1rem;
      cursor: pointer;
      border-radius: 4px;
      transition: background-color 0.3s;
    }

    #new-joke-btn:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div id="joke-container">
    <p id="joke-setup"></p>
    <p id="joke-punchline"></p>
    <button id="new-joke-btn" onclick="getRandomJoke()">Get Another Joke</button>
  </div>

  <script src="random_joke_generator.js"></script>
</body>
</html>
```

### JavaScript (`random_joke_generator.js`)
```js
async function getRandomJoke() {
  const response = await fetch('https://official-joke-api.appspot.com/random_joke');
  const data = await response.json();

  document.getElementById('joke-setup').innerText = data.setup;
  document.getElementById('joke-punchline').innerText = data.punchline;
}

getRandomJoke();
```
### Enjoy the Laughter!
We hope you enjoy the random jokes and have a great time using the Random Joke Generator! Feel free to contribute or share your own favorite jokes!

