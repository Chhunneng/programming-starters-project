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
<html>
  <head>
    <!-- Loading The Bootstrap Library -->
    <link rel="stylesheet" 
          href=
"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" 
          integrity=
"sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" 
          crossorigin="anonymous"/>

    <!-- Loading Icons From Font Awesome -->
    <link rel="stylesheet" 
          href=
"https://use.fontawesome.com/releases/v5.8.1/css/all.css" 
          integrity=
"sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" 
          crossorigin="anonymous">

    <!-- Loading Roboto Font from Google Fonts -->
    <link href=
"https://fonts.googleapis.com/css2?family=Roboto&display=swap" 
          rel="stylesheet">

    <!-- Loading Open Sans Font from Google Fonts -->
    <link href=
"https://fonts.googleapis.com/css2?family=Open+Sans+Condensed:wght@300&display=swap" 
          rel="stylesheet">

          <style>
                            *{
                    margin:0;
                    padding:0;
                    box-sizing: border-box;
                }

                body{
                    min-height:100vh;
                    transition: 0.5s;
                    transition-timing-function: ease-in;
                    background-image: linear-gradient(to right bottom, #ed4264a8, #ffedbca8);
                }
                
                .quote-box{
                    padding:3rem;
                    transition: 0.5s;
                    transition-timing-function: ease-in;
                }
                
                .text{
                    font-size:30px;
                    padding-left:10px;
                    transition: 0.5s;
                    transition-timing-function: ease-in;
                    font-family: 'Roboto', sans-serif;
                    background-image: linear-gradient(to right bottom, #ed4264a8, #ffedbca8);
                    color: transparent;
                    -webkit-background-clip: text;
                }

                .quote{
                    transition: 0.5s;
                    transition-timing-function: ease-in;
                }

                .new-quote{
                    font-size:15px;
                    border-radius: 5px;
                    cursor:pointer;
                    padding-bottom: 8px;
                    padding-top: 9px;
                    margin-top: 5px;
                    background-image: linear-gradient(to right bottom, #ed4264a8, #ffedbca8);
                }

                .text-center{
                    text-align: center;
                }
                
                .new-quote:hover{
                    opacity: 0.6;
                }

                .author{
                    margin:10px;
                    font-size:20px;
                    transition: 0.5s;
                    transition-timing-function: ease-in;
                    font-family: 'Open Sans Condensed', sans-serif;
                    background-image: linear-gradient(to right bottom, #28313B,#485461
                    );
                    color: transparent;
                    -webkit-background-clip: text;
                }
                
                
                p{
                    margin-top: 5px;
                    text-align: center;
                    position: absolute;
                    width: 100%;
                    top:21.5%;
                }

                .block {
                perspective: 150rem;
                position: absolute;
                top:25%;
                left: 27%;
                }

                .block__main {
                    min-width: 45vw;
                    position: absolute;
                    transition: all .8s ease;
                    backface-visibility: hidden;
                    box-shadow: 0rem 1.5rem 4rem rgba(0, 0, 0, 0.15);
                    border-radius: .5rem; 
                    background-image: linear-gradient(to right bottom, #F6F0EA,#F1DFD1);
                }

                .block__back {
                    transform: rotateY(180deg); 
                }

                .rotateF{
                transform: rotateY(-180deg);
                }

                .rotateB{
                transform: rotateY(0deg);
                }

          </style>
  
  </head>

  <body id="body">
    <div>

    <!-- Quote Box -->
    <div class="block text-center">

      <!-- Front part of the Quote Box -->
    <div class = "quote-box block__main block__front">

      <!-- Quote to be Displayed Here -->
      <span class = "quote">
        
        <!-- Hyphen is Displayed  -->
        <i class="fas fa-2x fa-quote-left"></i>

        <!-- Quote Text -->
        <span class = "text">
        Quote To be Displayed Here
        </span>

      </span>
      
      <!-- Author to be Displayed Here -->
      <div class = "author">
        Author to be Displayed Here
      </div>
      <a  class = "new-quote btn btn-default" 
          onclick="newQuote()">New Quote</a>
    </div>

    <!-- Back Part of the Quote Box -->
    <div class = "quote-box block__main block__back">

      <!-- Quote to be Displayed Here -->
      <span class = "quote">
        
        <!-- Hyphen is Displayed  -->
        <i class="fas fa-2x fa-quote-left"></i>

        <!-- Quote Text -->
        <span class = "text">
        Quote To be Displayed Here
        </span>

      </span>
      
      <!-- Author to be Displayed Here -->
      <div class = "author">
        Author to be Displayed Here
      </div>
        <!-- Button -->
        <a  class = "new-quote btn btn-default " 
            onclick="newQuote()">New Quote</a>
    </div>
  </div>
</div>
  
  <!-- Linking Your JavaScript File -->
  <script src="random_quote_generator.js"></script>
  </body>
  
</html>
```

### JavaScript (random_quote_generator.js)

```js (random_quote_generator.js)
        // Global Variable used to store the quotes 
        // fetched from the API
        var data;
        let front = true;

        // Getting the front and the back author boxes
        const authors = document.querySelectorAll(".author");

        // Getting the front and the back texts
        const texts = document.querySelectorAll(".text");

        // Getting the body
        const body = document.getElementById("body");

        // Getting the buttons
        const button = document.querySelectorAll(".new-quote");

        const blockFront = document.querySelector(".block__front");
        const blockBack = document.querySelector(".block__back");

        const authorFront = authors[0];
        const authorBack = authors[1];

        const textFront = texts[0];
        const textBack = texts[1];

        const buttonFront = button[0];
        const buttonBack = button[1];


        // An arrow function used to get a quote randomly
        const displayQuote = () =>{

            // Generates a random number between 0 
            // and the length of the dataset
            let index = Math.floor(Math.random()*data.length);

            // Stores the quote present at the randomly generated index
            let quote = data[index].text;

            // Stores the author of the respective quote
            let author = data[index].author;

            // Making the author anonymous if no author is present
            if(!author){
                author = "Anonymous"
            }

            // Replacing the current quote and the author with a new one

            if(front){
                // Changing the front if back-side is displayed
                textFront.innerHTML = quote;
                authorFront.innerHTML = author;
            }else{
                // Changing the back if front-side is displayed
                textBack.innerHTML = quote;
                authorBack.innerHTML = author;
            }
            
            front = !front;

        }

        // Fetching the quotes from the type.fit API using promises
        fetch("https://type.fit/api/quotes")
            .then(function(response) {
                return response.json(); 
            }) // Getting the raw JSON data
            .then(function(data) {

                // Storing the quotes internally upon 
                // successful completion of request
                this.data = data; 

                // Displaying the quote When the Webpage loads
                displayQuote() 
        });


        // Adding an onclick listener for the button
        function newQuote(){
            
            // Rotating the Quote Box
            blockBack.classList.toggle('rotateB');
            blockFront.classList.toggle('rotateF');

            // Displaying a new quote when the webpage loads
            displayQuote();
        }
```

Feel free to customize the random quote generator, add features, or modify the structure as you see fit. Contributors can use this document as a guide to implementing the random quote generator in JavaScript.
