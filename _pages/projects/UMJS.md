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

1. Add usersRepo and require
2. destructure the req to get all the things
3. await getOneBy `await usersRepo.getOneBy({email})`
4. add async

## Section 28: Production-Grade Authentication

- Hit log in and submitting the form just like above
- The BROWSER is going to collect information from the FORM
- It is going to SEND that information to the SERVER via a POST REQUEST

NOW, we can look at the `session` in NETWORK and look at the `RESPONSE HEADERS`

### 374. Cookie Based Authentication

### 375. Creating User Records

1. create user in user repo
   1. `await usersRepo.create({ email, password})`
   2. RETURN addrs from create
2. store id of that user and store it inside the users cookie
   1. Managing cookies is hard and so we are going to use another library
   2. npm install cookie-session

- before `await userRepo.create({email, password}`
- )

### 376. Fetching a Session

1. require cookiesession (its middleweare so we need to....)
2. `app.use(cookieSession({ keys:['sdlfkjsdflskjdf']}))`
3. `req.session` is an object from cookie-session
4. req.sesion.userId = user.id;

[BUG WITH NODEMON REFRESHING USERS.JSON](https://stackoverflow.com/questions/24120004/nodemon-exclusion-of-files)

Fixed by adding below to `package.json`:

```javascript
  "nodemonConfig": {
    "ignore": [
      "users.json"
    ]
  }
```

### 377. Signing Out a User

1. add /signin
2. add /signout
3. copy form from signin

### 378. Signing In

1. get email and password from req.body
2. take email check to see if email already exists via getOneBy()
3.

### 379. Hashing Passwords

PROBLEM: passwords aren't secured. Doesn't matter that this is a small app because people reuse passwords!

SOLUTION: Hashing algorithm

### 380. Salting Passwords

PROBLEM: Rainbow table attacks!!

SOLUTION: Salting!

### 381. Salting + Hashing Passwords

- crypto.randomBytes
- crypto.scrypt
- utils promisify

salt = crypto.randomBytes(8).toString('hex)
scrypt(attrs.password, salt, 64, (err, buff) => {
const hashed = buff.toString('hex')
})

1. generate salt
2. generate hashed password
3. save new hased password as record
4. return the record

### 382. Comparing Hashed Passwords

1. async comparePasswords(saved, supplied)
2. create new method
3. destructure
4. return
5. profit

### 383. Testing the Full Flow

1. update return of scrypt to reflect that it returns a buffer

## Section 29: Structuring Javascript Projects

### 384. Project Structure

### 385. Structure Refactor

1. make new file for auth routes in routes/admin/auth.js
2. migrate all auth routes to new file
3. confirm we are requiring things we need (usersRepo)
4. hook new file into express with `router`
5. replace all occourance of `app` with `router`
6. export router
7. back in index.js, below the middlewear, get the export we just made

THINGS I FORGOT

module.exports = router;

### 386. HTML Templating Functions

1. views > admin > auth > sign in & sign up
2. modeule. exports = ({req} => { return `our form`})
3. import singupTemplate
4. res.send(signupTemplate({req}))

### 387. HTML Reuse with Layouts

PROBLEM: So much of this is not DRY

SOLUTION: Layout file!

### 388. Building a Layout File

GOAL: reuse of html elements

admin > layout.js

### 389. Adding Better Form Validation

express-validator
pass an array to second argument

### 390. Validation vs Sanitization

destructure the one function we care about
const {check} = require('express-validator')

validator.js is being used by express-validator

### 391. Receiving Validation Output

### 392. Adding Custom Validators

express-validator checking password confirmation checking if email is in use

### 393. Extracting Validation Chains

### 394. Displaying Error Messages

const getError in validators

### 395. Validation Around Sign In

inSIGNIN
checkemail
checkpassword

### 396. Password Validation

### 397. Template Helper Functions

### 398. Adding Some Styling

### 399. Exposing Public Directories

public folder!
public >> css

Make folder available by this!!

`app.use(express.static('public'))`

### 400. Next Steps

### 401. Product Routes

/admin/products

/admin/products/new

router.get('/'

require productsRouter

1. Build new file `products.js`
2. like `admin.js`
3. Add two routes above
4. require it back inside our main express file

### 402. The Products Repository

OBJECT ORIENTED APPROACH

Users AND products EXTEND the Product CLASS!!

Repo.js

ALL methods to be shared

class Repository
Pastefrom constructor to bottom

Remove `create` and `comparePasswords`

add fs and crypto

Require in rhe repository and extends Repository
means we are go

_EXTENDS_

Means "take a look at that class repository and all the different motheds that have been assigned to it and we can copy and paste them into the body of our class

EXTENDS essentially means that we are copying and pasting all the methods from (whatever we are extending) to (whereever we are usign the extend)

add a generic async CREATE method

1. Create new file repository.js
2. Remove all except `create` and `change password` from user repo
3. Add new create method to repository,js

### 403. Code Reuse with Classes

### 404. Creating the Products Repository

productsrepo extends repo

1. create new products.js
2. have it extend repo
3. go into routes
4. require the products repo inside the products route

### 405. Building the Product Creation Form

views >> admin >> products >> new.js

const layout = require layout

const get error = require helpers

module.exports = ({ errors }) => {
return layout({ content: ``})
}

productsNewTemplate

res.send inside /new
productsNewTemplate({})

1. Create new `new.js` page
2. require layout and get error
3. return content in layout
4. inside prouct routes, grab that new template

### 406. Some Quick Validation

Require title
.trim()
.isLength({ min: 5, max: 40 })

Require price
.trim()
.toFloat()
.isFloat()

from products, require validators

Now make a post request handlersecond argument is array with validators and then req and res and res .

validationResult from express-validator

## Section 30: Image and File Upload

### 407. Exploring Image Upload

add withMessage()

### 408. Understanding Mutli-Part Forms

**_IMPORTANT_**

How do you send an image in a form!?

`form method='POST' enctype="multipart/form-data"`

### 409. Accessing the Uploaded File

`npm install multer`

### 410. [Optional] Different Methods of Image Storage

[OMG SERIOUSLY BEST IMAGE VIDEO EVER](https://www.udemy.com/course/javascript-beginners-complete-tutorial/learn/lecture/17007522#overview)

### 411. Saving the Image

1. buffer.toString()
2. `const image = req.file.buffer.toString("base64");`
3. add to product json file using product repo

### 412. A Subtle Middleware Bug

Middlewares operate in a very specific order! We need to swap them to deal with this bug

```javascript
// BEFORE
router.post(
  "/admin/products/new",
  [requireTitle, requirePrice],
  upload.single("image"),
  async (req, res) => {...

// AFTER

router.post(
  "/admin/products/new",
  [requireTitle, requirePrice],
  upload.single("image"),
  async (req, res) => {...

router.post(
  "/admin/products/new",
  upload.single("image"),
  [requireTitle, requirePrice],
  async (req, res) => {

```

### 413. Better Styling

### 414. Reusable Error Handling Middleware

Organize our middlewares!!

routes >> admin >> middlewares.js

```javascript
module.exports = {
  handleErrors(templateFunc) {
    return (req, res, next) => {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.send(templateFunc({ errors }));
      }
      next();
    };
  },
};
```

we MUST return a function because middlewares MUST be a function!!

const { handle errors } top of products js

handleErrors(productsNewTemplate)
WITHOUT function parens becuase we're passing a REFERENCE to the function

PROBLEM: Our error handling isn't DRY!

SOLUTION: add a DIY `handleErrors()` middleware!

1. create new middlware file and function in routes/admin
2. Require that function in routes/admin auth and products
3. update the error-handling requests to use our new handleErrors middleware and delete old code!

### 415. Products Listing

Build a list using a map statement
for every product we are going to generate an HTML snippet,
Leading to an array of HTML snippets, which will will join together into a big string

### 416. Redirect on Success Actions

`res.redirect`

login
signup

### 417. Requiring Authentication

CODE DUPLICATION MEANS MIDDLEWARE!!!

add requireAuth (req, res, next) to middlewares

```javascript
// BEFORE

router.get("/admin/products", async (req, res) => {
  if (!req.session.userId) {
    return res.redirect("/signin");
  }
  const products = await productsRepo.getAll();
  res.send(productsIndexTemplate({ products }));
});

// AFTER

router.get("/admin/products", requireAuth, async (req, res) => {
  const products = await productsRepo.getAll();
  res.send(productsIndexTemplate({ products }));
});
```

### 418. Template Update

### 419. Ids in URLs

Add id to edit button on products index

### 420. Receiving URL Params

NOW we need to make our route handler to handle the edit we just created above!

router.get('/admin/products/:id/edit)

:thing means WILDCARD!!

Now get product out of productsrepository using GET ONE

mark function async
await products Repo.getOne(req.params.id)

### 421. Displaying an Edit Form

1. update edit form to include the "handle errors" function
2. add a second param to our handle errors function inside product router

## Section 31: Building a Shopping Cart

### 422. Editing a Product

### 423. Fixing the HandleErrors Middleware

### 424. Edit Form Template

### 425. Deleting Products

Done

### 426. Starting with Seed Data

Done

### 427. User-Facing Products

routes > products

require express
create new couter

associate route with get to route route

pass in async function

module.exports = router

roots.js

add

### 428. Products Index

### 429. Merging More Styling

### 430. Understanding a Shopping Cart

### 431. Solving Problem #1

PROBLEM: How do we tie cart to non-logged in user?!

SOLUTION: COOKIES!!

### 432. Solving Problem #2

PROBLEM: How do we tie a product to a cart??!

THREE DIFFERENT APPROACHES:
Bad options first!!

BAD #1 -- add a "Carts" array to each product

BAD #2 -- Carts repository

GOOD!! -- Carts repository that simply points to the product id

### 433. Shopping Cart Boilerplate

1. new routes file >> carts.js
   1. express
   2. router
   3. module.exports = router;
   4. IN INDEX.JS add carts router to app.use(cartsRouter)
2. views directory
3. new repo >> carts.js (same as products to start)

--
ROUTES

1. Add to cart POST
2. Show cart GET
3. delete from cart POST

--
TODO

1. Add repo
2. Add router
3. require router
4. Add comments

### 434. Submission Options

Now we are going to take the product id and assign it to a cart

1. Take product id, assign to cart stored in our carts repository
2. we want to find the cart assoiated with this user
3. Take a look at the aitems array and add a new item or new object that represents the prodcut

TWO SCENARIOS:

1. Firsttime user -- no cart for user!
   1. Must CREATE CART
   2. then ADD TO CART
2. Returning user --
   1. Must FIND CARD
   2. then ADD TO CART

### 435. Creating a Cart, One Way or Another

### 436. Adding Items to a Cart

### 437. Displaying Cart Items

router get '/cart'

if not req.session.cartId
return res.redirect('/')
const cart = await cartsRepo.getOne(req.session.cartId)

### 438. Rendering the List

### 439. Totaling Cart Items

### 440. Removing Cart Items

### 441. Redirect on Remove

## Section 32: The Basics of Testing

## Section 33: Building a Testing Framework From Scratch

## Section 34: Bonus!
