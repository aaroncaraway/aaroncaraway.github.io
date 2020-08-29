---
layout: single
title: "UWD"
permalink: /pages/UWD
tags: UWD
classes: wide
---

# OUTLINE

## Section 1: Front-End Web Development

## Section 2: Introduction to HTML

## Section 3: Intermediate HTML

## Section 4: Introduction to CSS

## Section 5: Intermediate CSS

## Section 6: Introduction to Bootstrap 4

## Section 7: Intermediate Bootstrap

## Section 8: Web Design School - Create a Website that People Love

## Section 9: Introduction to Javascript ES6

## Section 10: Intermediate Javascript

## Section 11: The Document Object Model (DOM)

## Section 12: Boss Level Challenge 1 - The Dicee Game

## Section 13: Advanced Javascript and DOM Manipulation

## Section 14: jQuery

## Section 15: Boss Level Challenge 2 - The Simon Game

## Section 16: The Unix Command Line

## Section 17: Backend Web Development

## Section 18: Node.js

## Section 19: Express.js with Node.js

Most commonly used. "Extended: true" means we can pass nested objects

```javascript
app.use(bodyParser.urlencoded({ extended: true }));
```

All together now:

```javascript
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
```

## Section 20: APIs - Application Programming Interfaces

TODO:

kanye.rest

JOKE API
`https://sv443.net/jokeapi/v2/joke/Pun?blacklistFlags=nsfw&type=single`

### 257: Api auth and postman

1. Sign up for API key at openweather
2. Look at the structure of the API call

http://api.openweathermap.org/data/2.5/weather?q=London&appid=933d7d672525d0d55611b4587b398adb

### Making GET requests with Node HTTP module

1. Create new weather app
2. `touch index.html app.js`
3. `npm init`
4. `npm i express`
5. open in an editor
6. build out app.js
   1. require express
   2. app=express()
   3. app.listen(3000, function(){ callback})
   4. app.get('/', function)

#### ERRORS I GOT

`SyntaxError: Cannot use import statement outside a module`

FIXED

```javascript
// import express from "express";
// import https from "https";
const express = require("express");
const https = require("https");
```

also had to add

```javascript
  "scripts": {
    "start": "node app.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
```

to our start scripts. But really, this should be nodemon.

#### TINY EXAMPLE OF API REQUEST USING JUST EXPRESS AND NODE HTTPS MODULE

```javascript
const express = require("express");
const https = require("https");

const app = express();

app.get("/", (req, res) => {
  const url =
    "https://api.openweathermap.org/data/2.5/weather?q=Los Angeles&appid=933d7d672525d0d55611b4587b398adb&units=Imperial";
  https.get(url, (response) => {
    console.log(response);
  });
  res.send("HERE WE ARE!");
});

app.listen(3030, () => {
  console.log("listening on port 3030");
});
```

### 260. How to Parse JSON

IMPORTANT!!

To get readable data: `JSON.parse(data)`

To turn object into string: `JSON.stringify(data)`

```javascript
res.on("data", (d) => {
  console.log(d);
});
```

NOW, to actually read it...

```javascript
res.on("data", (d) => {
  const parsedData = JSON.parse(d);
  console.log(parsedData);
});
```

## Section 21: Git, Github and Version Control

## Section 22: EJS

## Section 23: Boss Level Challenge 3 - Blog Website

## Section 24: Databases

## Section 25: SQL

## Section 26: MongoDB

## Section 27: Mongoose

## Section 28: Putting Everything Together

## Section 29: Deploying Your Web Application

## Section 30: Boss Level Challenge 4 - Blog Website Upgrade

## Section 31: Build Your Own RESTful API From Scratch

## Section 32: Authentication & Security

## Section 33: React.js

## Section 34: Bonus Module: Ask Angela Anything

## Section 35: Next Steps
