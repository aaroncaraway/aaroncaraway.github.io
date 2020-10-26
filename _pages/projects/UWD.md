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

NOTE:

We can only have one `res.send` in any of the `app.get('/'....)`

HOWEVER, we can have as many `res.write` s as we want!

### MAILCHIMP API!

Challenge

1. mkdir
2. touch app.js signup.html success.html failure.html
3. npm init
4. npm i express request body-parser nodemon
5. update package json to include `"start":"nodemon app.js"`
6. add require statements to app.js

---

1. make signup page from bootstrap
2. require bootstrap cdn
3. change the input fields
4. update the input fields css
5. Get this to show up when we hit `/`

### 265. Posting Data to Mailchimp's Servers via their API

GOAL: go to mailchimp.com and see subscriber

- JSON.stringify(data
- Replace the X in the url
- check curl request for the url
- const options including method
- auth: "sldkfjsdlfkj:myApiKey"
- console.log JSON.parse
- request.write(request )

#### How to set Heroku Environment Variables

[heroku config:set API_KEY=sdlfjsdlfksjdlfkj](https://devcenter.heroku.com/articles/config-vars)

## Section 21: Git, Github and Version Control

## Section 22: EJS

[DOCS](https://github.com/mde/ejs/wiki/Using-EJS-with-Express)

todolist-v1
touch index.html
app.js
npm init
npm i express bodyparser

make template for express and body-parser

NOTE! We can only use `res.send()` once HOWEVER, we can use res.write as many times as we want!!

`res.write('thing')`
`res.write('thing')`
`res.send()`

we also have
`res.sendFile(__dirname + '/myfile.html')`

### TO USE EJS:

1. create a new folder called `views`
2. create `list.ejs`
3. Add this to `app.js`

```javascript
const app = express();
app.use("view engine", "ejs");
app.get("/", (req, res) => {
  res.render("list", { kindOfDay: day });
});
```

CHALLENGE:

1. Make new app with pages
2. Make boilerplate express docs
3. Add EJS
4. Add variable

### TO INCLUDE JS:

- use ejs "Scriplette" tag [Docs HERE](https://ejs.co/#docs)
- can ONLY use "control flow" (if/else) statements within `<% scriplette %>`

### UNDERSTANDING NODE EXPORTS & MODULES

#### INSIDE MODULE FOLDER

module.export = oneFunction;

module.export.functionOne = oneFunction

module.export.functionTwo = secondFunction

#### INSIDE APP.JS

let howEverWeRequiredIt = require('my_module')
howEverWeRequiredIt.oneFunction()


#### BUT to make everything EVEN MORE SUCCINCT...

module.exports.myFunction = function(){
  <!-- anonymous function -->
}

we can make it EVEN SHORTER using just `exports` instead of `module.exports`

we can use `const` for things like Arrays and Objects -- it protects the DATA STRUCTURE not the things inside it (which we CAN change)

We can't REASSIGN the array to a new things or the Object to a new thing, but we CAN change the insides of those things.

## Section 23: Boss Level Challenge 3 - Blog Website

## Section 24: Databases

## Section 25: SQL

## Section 26: MongoDB

## Section 27: Mongoose

### NOTES:

View db/collections:
`use my_db`
`show collections`

Find:
`db.collection-name.find()`

Drop db:
 `use my_db`
 `db.dropDatabase()`

 ---
### Insert MANY THINGS!!

 Insert an ARRAY 
`NameOfMongooseModel.insertMany([array], callback)`
`Person.insertMany()`

## Section 28: Putting Everything Together

## Section 29: Deploying Your Web Application

MongoDB Atlas

1. Create a cluster
2. Create a user (note un and pw)
3. security - network access - whitelist allow access from anywhere
4. cluster connect

mongo "mongodb+srv://cluster0.lived.mongodb.net/test" --username myusername

`show dbs`

`use test`

`show collects`

`db.test.findall`

### 376. Deploying an App with a Database to Heroku

Procfile

`web: node app.js`

it's just instructions
when on the web, use node to access app.js

Add version of node to package json

```json
"engines": {
  "node": "version number"
}
```

(to find version)
`node --version`

## Section 30: Boss Level Challenge 4 - Blog Website Upgrade

## Section 31: Build Your Own RESTful API From Scratch

### RESTFUL VERBS:

GET
POST
PUT & PATCH
DELETE

### RESTFUL + CRUD:

* GET == Read 



## Section 32: Authentication & Security

## Section 33: React.js

## Section 34: Bonus Module: Ask Angela Anything

## Section 35: Next Steps
