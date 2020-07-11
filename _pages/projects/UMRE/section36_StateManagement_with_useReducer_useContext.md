---
layout: single
title: "UMRE: Section 36, State Management w/ useReducer & useContext"
permalink: /pages/projects/UMRE/section36
tags: UMRE
classes: wide
---

# Section 36: State Management w/ useReducer & useContext

## 277. IMPORTANT: GET THE CODE HERE!

[here](https://github.com/Colt/todos-context-usereducer/tree/6-add-local-storage-reducer-hook)

## 278. Adding In Todos Context

- need familiarity with previous two sections
- Make a context to wrap around todos so we don't have to pass down forever!!

* Refactor as we go

## 279. Consuming the Todo Context

TodoForm
useCOntext(TodosContext )

TODO LIST

TODO

EDIT TODO FORM

## 280. The Issues w/ Our Current Approach

making MAGIC REDUCER FUNCTION

TODO FORM RENDER

add console logs to editTodoform
add console logs to todo form

PROBLEM: everything is rerending ALL the time. We don't need all that rerendering!

SOLUTION:

We will have two CONTEXTS
A context for STATE
and a context for METHODS!!

NOTE: We can see cool visuals for what's getting rerendered with react dev tools and "highlight"

## 281. WTF Is a Reducer

Simply a function that follows this pattern:
(accumulatedValue, nextItemInArray) => nextAccumulatedValue

TL;DR -- It takes two values and "reduces" them to one value

```javascript
const nums = [2, 4, 5, 8];
const theReducer = (accumulator, nextThing) => accumulator + nextThing;
nums.reduce(theReducer, 9);
```

In our case (in REACT) the two values provided to a reducer are:

1. The current state
2. An action that (may) update the state

(state, action) => newState

NOTE: It's complicated in terms of terminology but the idea is simple -- we write a single function, a single reducer that takes the existing state and some new action and then figures out what to return (in some ways, it's just a series of long conditionals or switch statements where you are checking is the action update todo or delete todos)

## 282. First useReducer Example

An alternative

{type: 'ADD_TODO', task: "Walk the Cat}

TL;DR: useReducer is simply a way of organizing stateful logic into one place (as well as updates to that state)

NOTE: Remember this is just a PATTERN. A PATTERN we will get familiar with.

## 283. Defining our Todo Reducer

## 284. Splitting Into 2 Contexts

## 285. Optimizing w/ Memo

## 286. Custom Hook: Reducer + LocalStorage
