---
layout: single
title: "UTS"
permalink: /pages/UTS
tags: UTS
classes: wide
---

## Section 1: Getting Started with Typescript

Typescript is like a friend sitting behind you while you code, helping you catch errors.

### INSTALL

`npm install -g typescript ts-node`

### TEST

`tsc --help`

### Visual Studio TypeScript Optimal Install

1. Add code to Path `View > Command Pallet > search "install path"`
2. Add prettier (via extensions)
3. Run prettier on save `Code > Settings > search "Format on save"`
4. Use Single Quotes with Prettier

### 4 -- Our First App

1. Look at API
2. Mkdir
3. make package.json
4. install axios for requests
5. write code!

### RUN THE THING!

`ts-node index.ts`

### 8 -- Catching Errors with Type Script

#### BEFORE

```javascript
import axios from "axios";

const url = "https://jsonplaceholder.typicode.com/todos/1";

axios.get(url).then((response) => {
  const todo = response.data;

  console.log(`
  The Todo with ID: ${todo.id}
  With the title of: ${todo.title}
  Is completed? ${todo.completed}
  `);
});
```

#### AFTER PT ONE

```javascript
import axios from "axios";

const url = "https://jsonplaceholder.typicode.com/todos/1";

interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

axios.get(url).then((response) => {
  const todo = response.data as Todo;

  const id = todo.id;
  const title = todo.title;
  const completed = todo.completed;

  console.log(`
    The Todo with ID: ${id}
    With the title of: ${title}
    Is completed? ${completed}
  `);
});

```

#### AFTER PT TWO

```javascript
import axios from "axios";

const url = "https://jsonplaceholder.typicode.com/todos/1";

interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

axios.get(url).then((response) => {
  const todo = response.data as Todo;

  const id = todo.id;
  const title = todo.title;
  const completed = todo.completed;

  logTodo(id, title, completed);
});

const logTodo = (id: number, title: string, completed: boolean) => {
  console.log(`
  The Todo with ID: ${id}
  With the title of: ${title}
  Is completed? ${completed}
`);
};

```

## Section 2: What is a Type System?

### FLATLIST!!

PROPS:

- horizontal: changes scroll direction from vertical to horizontal
- showsHorizontalScrollIndicator={false}: removes the scroll bar from the bottom

EXAMPLE:

```javascript
<FlatList
  horizontal
  showsHorizontalScrollIndicator={false}
  keyExtractor={(friend) => friend.name}
  data={friends}
  renderItem={({ item }) => <Text style={styles.textStyle}>{item.name}</Text>}
/>
```

## Section 3: Type Annotations in Action

## Section 4: Annotations With Functions and Objects

## Section 5: Mastering Typed Arrays

## Section 6: Tuples in Typescript

## Section 7: The All-Important Interface

## Section 8: Building Functionality with Classes

## Section 9: Design Patterns with Typescript

## Section 10: More on Design Patterns

## Section 11: Reusable Code

## Section 12: Advanced Generics

## Section 13: Let's Build a Web Framework

## Section 14: Express + Typescript Integration

## Section 15: Decorators

## Section 16: Advanced Express and TS Integration

## Section 17: React and Redux with Typescript

## Section 18: Extras
