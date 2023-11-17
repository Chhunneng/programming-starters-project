# Random Quote Generator in JavaScript

Welcome to the Random Quote Generator project for JavaScript! 🚀

In this project, we'll create a simple web page that displays random quotes. Let's get started!

## Project Overview

### Objective

Create a JavaScript script that fetches and displays random quotes from an API.

### Features

- Fetch random quotes from a public API.
- Display the quotes dynamically on a web page.
- Allow users to refresh the page to get a new random quote.

## Project Structure

Create a new HTML file named `index.html` and a JavaScript file named `random_quote_generator.js`.

## Instructions

1. **Set Up HTML Structure:**
   - Create an HTML file with a basic structure, including an area to display the random quote.

2. **Fetch Quotes from API:**
   - Use JavaScript to fetch random quotes from a public API (e.g., [Quotable API](https://api.quotable.io/random)).

3. **Display Quotes Dynamically:**
   - Update the HTML content dynamically to display the fetched quotes.

4. **Handle Page Refresh:**
   - Allow users to refresh the page to get a new random quote.

5. **Run the Script:**
   - Open the HTML file in a web browser to see the random quotes in action.

## Example Code

### HTML (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Random Quote Generator</title>
</head>
<body>
  <div id="quote-container">
    <p id="quote-text"></p>
    <p id="quote-author"></p>
    <button onclick="getRandomQuote()">Get Another Quote</button>
  </div>

  <script src="random_quote_generator.js"></script>
</body>
</html>
```

### JavaScript (random_quote_generator.js)

```js
// Function to fetch a random quote from the Quotable API
async function getRandomQuote() {
  const response = await fetch('https://api.quotable.io/random');
  const data = await response.json();

  // Update HTML content with the fetched quote
  document.getElementById('quote-text').innerText = data.content;
  document.getElementById('quote-author').innerText = `- ${data.author}`;
}

// Initial call to get a random quote when the page loads
getRandomQuote();
```

Feel free to customize the random quote generator, add features, or modify the structure as you see fit. Contributors can use this document as a guide to implementing the random quote generator in JavaScript.
