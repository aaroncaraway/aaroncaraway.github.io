---
layout: single
title: "UWD"
permalink: /pages/UMJS
tags: UWD
classes: wide
---

## Section 1: Introduction

## Section 2: JS Values & Variables

- PROPERTIES = values we can access

`"hello".length` -- `length` is property of string `"hello"`

- Strings are immutable in JS

- METHODS = actions that can be performed on/with (format: `string.method()`)

## Section 3: How to Model Data Efficiently

## Section 4: Controlling Program Logic and Flow

## Section 5: Capture Collections of Data with Arrays

## Section 6: Objects - The Core of Javascript

## Section 7: The World of Loops

## Section 8: Writing Reusable Code with Functions

## Section 9: An Advanced Look at Functions

## Section 10: Apply Functions to Collections of Data

## Section 11: A Few Miscellaneous JS Features

## Section 12: Object Methods and the 'This' Keyword

## Section 13: JS In the Browser - DOM Manipulation

## Section 14: Twisting the DOM to Our Will!

## Section 15: Communicating with Events

## Section 16: Asynchronous Code, Callbacks & Promises

## Section 17: Making HTTP Requests

## Section 18: Async & Await: JS Magic

## Section 19: Prototypes, Classes, & The New Operator

## Section 20: Drawing Animations

## Section 21: Application Design Patterns

## Section 22: Javascript with the Canvas API

## Section 23: Make a Secret-Message Sharing App

## Section 24: Create Node JS Command Line Tools

### THINGS WE USED

- `lstat`
- `utils`
- `chalk`
- `path`

* File sharing happens with module.export makes files available
* Require lets us access what we see in module.export

NOTE: `arguments` is a great key word to inspect what we are looking at

#### Invisible Node Functions

- export
- require
- \_\_filename
- \_\_dirname

#### Debugging with node

chrome://inspect
`node --inspect-brk index.js`

### HIGH POINTS: THINGS WE LEARNED

- Commands in package json (`bin`)
- Package.json tracks dependencies

## Section 25: Create Your Own Project Runner

### THINGS WE USED:

- lodash.debounce

Creating a `nodemon` clone!
same start as above

### BIG APP ISSUES:

- Need to detect when a file changes
- Want to add help for other devs
- Need to run JS code from within a JS program

--

#### So we will use other libraries!

- Need to detect when a file changes --> `chokidar`
- Want to add help for other devs --> `caporal`
- Need to run JS code from within a JS program --> `child_process`

* DEBOUNCING (we add in a waiting timer)

### 345. Ensuring Files Exist

1. Move functionality into caporal
2. Sub console logs with `start` function
3. destructure to find {filename}
4. Make that function async
5. Require fs.promises to find the file name
6. wrap that in a try catch

### 346. It works!

1. GOAL: make test file and change test file to see it working
2. use child_process {spawn}

### 348. More on Child_Process

1. `spawn` does mostly everything we will need
2. `fork` will be used for webservers!

### 349. App Wrapup

1. kill old programs
2. if(proc\_ proc.kill())
3. we can use chalk again

## Section 26: Project Start - E-Commerce App

### 351. App Architecture

PROJECT SETUP:

1. Create a new project directory
2. Generate package.json `npm init -y`
3. Add node modules
4. Create a start script to run our project!

### 352. Package.json scripts

1. `npm run dev` is goal
2. add `"dev": "nodemon index.js"` to scripts in package.json

### 353. Creating a Web Server

What is express?

```javascript
// app.get("/", CALLBACK FUNCTION;
app.get("/", (req, res) => {});

// app.listen(PORT, CALLBACK)
app.listen(3000, () => {
  console.log("Listening!");
});
```

REQ = REQUEST, an incoming request from the browser
RES = RESPONSE, the outgoing response

REQ -- If we need info from the user
RES -- If we ever need to send information back to the browser

### 356. Understanding Form Submissions

GOAL: form submission with response

1. Create res.get
2. Create.res.post
3. profit

### 357. Parsing Form Data

GOAL: Save email, password and password confirmation on our server

NOTE: `req.on` is very similar to `addEventListener`

- So we're saying we want to run some callback function when some event occurs.
- `req.on('data', data => {})` is waiting for the DATA EVENT.
- The request object emits a data event any time it receives some bit of data
- That data is passed in as the first argument to the callback function

```javascript
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.send(`<div>
  <form method='POST'>
    <input name="email" type="email" />
    <input name="password" type="password" />
    <input name="passwordConfirmation" type="password" />
    <button>Submit</button>  
  </form>
  </div>`);
});

app.post("/", (req, res) => {
  req.on("data", (data) => {
    console.log(data);
  });
  res.send("ACCOUNT CREATED!!");
});

app.listen(3000, () => {
  console.log("listening!");
});
```

PROBLEM: When we first get the data back in our terminal after this console log, it is in a very RAW formmat (it comes back in an array of raw information)

SOLUTION:

```javascript
app.post("/", (req, res) => {
  req.on("data", (data) => {
    console.log(data.toString("utf8"));
  });
  res.send("ACCOUNT CREATED!!");
});
```

### 358. Middlewares in Express

WHAT IS MIDDLEWARE!?
Function that preprocesses the `req` and `res` objects!! Helping to reduce code repeats!!

```javascript
app.post("/", bodyParser, middleWare2, mw3, (req, res) => {}
```

- BODYPARSER is middleware!!
- Made before promises were popular, it gives us NEXT to access the callback function

```javascript
// bodyParser = (req, res, CALLBACK)
const bodyParser = ((req, res, next) = {});
```

--- BEFORE

```javascript
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.send(`<div>
  <form method='POST'>
    <input name="email" type="email" />
    <input name="password" type="password" />
    <input name="passwordConfirmation" type="password" />
    <button>Submit</button>  
  </form>
  </div>`);
});

const bodyParser = (req, res, next) => {
  if (req.method == "POST") {
    req.on("data", (data) => {
      const parsed = data.toString("utf8").split("&");
      const formData = {};
      for (let pair of parsed) {
        const [key, value] = pair.split("=");
        formData[key] = value;
      }

      req.body = formData;
      next();
    });
  } else {
    next();
  }
};

app.post("/", bodyParser, (req, res) => {
  console.log(req.body);
  res.send("ACCOUNT CREATED!!");
});

app.listen(3000, () => {
  console.log("listening!");
});
```

### 359. Globally Applying Middleware

BEFORE:

`bodyParser.urlencoded({ extended: true})`

```javascript
// GOOD: our DIY parser
app.post("/", bodyParser, (req, res) => {
  console.log(req.body);
  res.send("ACCOUNT CREATED!!");
});

// BETTER: Using the parser from the library!
app.post("/", bodyParser.urlencoded({ extended: true }), (req, res) => {
  console.log(req.body);
  res.send("ACCOUNT CREATED!!");
});

// BEST: Adding bodyParser to the WHOLE APP
app.use(bodyParser.urlencoded({ extended: true }));
```

## Section 27: Design a Custom Database

### 360. Data Storage

We need to STORE information somewhere.
We need it to be PERSISTENT

### 361. Different Data Modeling Approaches

### 362. Implementing the Users Repository

METHODS USED:

- fs.asscessSync
- fs.writeFileSync

NOTE: We are NOT allowed to have async code inside a `constructor` (This is one of the only times using fs.\_\_Sync functions is OK)

GOAL: Create & Implement a Users repository

1. make folder
2. make users.js file
3. make class
4. test class
5. put constructor
6. add try catch with fs.acscess and fswriteFile

### 363. Opening the Repo Data File

1. Open the file
2. Read the contents
3. Parse the Contents
4. Return the parsed data

### 364. Small Refactor

```javascript
// BEFORE
  async getAll() {
    const contents = await fs.promises.readFile(this.filename, {
      encoding: "utf8",
    });

    const data = await JSON.parse(contents);
    return data;
  }
// AFTER
  async getAll() {
    return JSON.parse(
      await fs.promises.readFile(this.filename, {
        encoding: "utf8",
      })
    );
  }

```

### 365. Saving Records

1. make create function
2. use writefile
3. with attrs for attributes
4. test it by adding file before

```javascript
const fs = require("fs");

class UsersRepository {
  constructor(filename) {
    if (!filename) {
      throw new Error("Creating a repository requires a filename");
    }

    this.filename = filename;
    try {
      fs.accessSync(this.filename);
    } catch (err) {
      fs.writeFileSync(this.filename, "[]");
    }
  }

  async getAll() {
    return JSON.parse(
      await fs.promises.readFile(this.filename, {
        encoding: "utf8",
      })
    );
  }

  async create(attrs) {
    const records = await this.getAll();
    records.push(attrs);

    await fs.promises.writeFile(this.filename, JSON.stringify(records));
  }
}

const test = async () => {
  const repo = new UsersRepository("users.json");

  await repo.create({ email: "test@test.com", password: "password" });

  const users = await repo.getAll();

  console.log(users);
};

test();
```

NOTE: it is `accessSync` not `accessFileSync` (this was overwriting my values and giving me major errors)

### 366. Better JSON Formatting

```javascript
// JSON.stringify(data, FUNCTION, SPACES)
JSON.stringify(records, null, 2);
```

### 367. Random ID Generation

PROBLEM: We don't have unique IDs!

SOLUTION: create a RandomID method

### 368. Finding By Id

use find
get a user id from user.json

### 369. Deleting Records

use filter

### 370. Updating Records

### 371. Adding Filtering Logic

### 372. Exporting an Instance

```javascript
// potentially buggy
module.exports = UsersRepository;
// less buggy for our purposes
module.exports = new UsersRepository("users.json");
```

CLEANING UP AND REMOVING TESTS!

```javascript
// const test = async () => {
//   const repo = new UsersRepository("users.json");
//   //   TESTING CREATE + GET ALL
//   //   await repo.create({ email: "catmom@gmail", password: "ilovecats" });
//   //   const users = await repo.getAll();
//   //   console.log(users);

//   //  TESTING GETONE
//   //   const user = await repo.getOne("fbdeba1c");
//   //   console.log(user);

//   //  TESTING DELETE
//   //   await repo.delete("2675571a");

//   // TESTING UPDATE
//   //   await repo.create({ email: "turtlemom@gmail" });
//   //   await repo.update("e72f6a67", { password: "iloveturtles" });
//   //  TESTING GETONEBY

//   const user = await repo.getOneBy({ email: "turtlemom@gmail" });
//   console.log(user);
// };

// test();
```

### 373. Signup Validation Logic

## Section 28: Production-Grade Authentication

## Section 29: Structuring Javascript Projects

## Section 30: Image and File Upload

## Section 31: Building a Shopping Cart

## Section 32: The Basics of Testing

## Section 33: Building a Testing Framework From Scratch

## Section 34: Bonus!
