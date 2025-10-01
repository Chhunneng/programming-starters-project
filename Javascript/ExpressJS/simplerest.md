# Simple REST API with Express.js

In this tutorial, we will create a simple REST API using Express.js, a popular Node.js framework.

## Prerequisites

- Node.js installed
- Basic knowledge of JavaScript

## Step 1: Initialize the Project

First, create a new directory for your project and navigate into it:

```bash
mkdir simplerest
cd simplerest
```

Next, initialize a new Node.js project:

```bash
npm init -y
```

Then, install Express.js:

```bash
npm install express
```

## Step 2: Create the Server

Create a new file named `server.js` and add the following code to set up a basic Express server:

```javascript
const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
```

## Step 3: Run the Server

To start the server, run the following command in your project directory:

```bash
node server.js
```

You should see the message `Server is running on http://localhost:3000` in your terminal. Open your browser and navigate to `http://localhost:3000` to see the "Hello World!" message.
