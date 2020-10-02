---
layout: single
title: "TEMPLATES"
permalink: /pages/templates
classes: wide
---

## EXPRESS

### BASIC (urlencoding for FORMS - ala UWD)

```javascript
const express = require("express");
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.send("hello there!");
});

let port = 4242;
app.listen(port, () => {
  console.log(`currently listening on port ${port}`);
});
```

### BASIC PLUS (WITH JSON -- ala UMJS)

```javascript
const express = require("express");
const bodyParser = require("body-parser");
const { randomBytes } = require("crypto");
const cors = require("cors");

const app = express();
app.use(bodyParser.json());
app.use(cors());

const posts = {};

app.get("/posts", (req, res) => {
  res.send(posts);
});

app.post("/posts", (req, res) => {
  const id = randomBytes(4).toString("hex");
  const { title } = req.body;
  console.log("getting here", id, title);

  posts[id] = {
    id,
    title,
  };
  res.status(201).send(posts[id]);
});

app.listen(4000, () => {
  console.log("currently listening on port 4000");
});
```

### `res`

`res.send()`
`res.write()`
`res.sendFile(__dirname)`

## EXPRESS + EJS

### -- app.js

```javascript
//jshint esversion:6
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.set("view engine", "ejs");

const dayWords = {
  0: "Sunday",
  1: "Monday",
  2: "Tuesday",
  3: "Wednesday",
  4: "Thursday",
  5: "Friday",
  6: "Saturday",
};

app.get("/", (req, res) => {
  const today = new Date();
  const day = today.getDay();

  res.render("list", { currentDay: dayWords[day] });
});

app.post("/", (req, res) => {
  res.send(req.body.greeting);
});

app.listen(4040, () => {
  console.log("currently listening on port 4040");
});
```

### -- views/list.ejs

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>TODO V1</title>
  </head>
  <body>
    <h1>Today is <%= currentDay %></h1>
    <form action="/" method="post">
      <input type="text" name="greeting" />
      <button type="submit">SUBMIT</button>
    </form>
  </body>
</html>
```

### -- package.json

```json
{
  "name": "uwd-todo-v1",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "start": "nodemon app.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "body-parser": "^1.19.0",
    "ejs": "^3.1.5",
    "express": "^4.17.1",
    "nodemon": "^2.0.4"
  }
}
```

### -- For URN

```javascript
import React from "react";
import { View, Text, StyleSheet } from "react-native";

const ListScreen = () => {
  const name = "Obi Wan";
  return <Text>List Screen</Text>;
};

const styles = StyleSheet.create({});

export default ListScreen;
```
