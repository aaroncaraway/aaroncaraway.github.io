---
layout: single
title: "TEMPLATES"
permalink: /pages/templates
classes: wide
---

## EXPRESS

### BASIC

```javascript
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.send("hello there!");
});

app.listen(4040, () => {
  console.log("currently listening on port 4040");
});
```

### BASIC PLUS

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
