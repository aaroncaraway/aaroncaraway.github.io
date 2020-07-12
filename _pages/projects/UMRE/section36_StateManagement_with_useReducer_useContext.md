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

NOTE: It's complicated in terms of terminology but the idea is simple -- we write a single function, a single reducer that takes the existing state and some new action and then figures out what to return (in some ways, it's jusaat a series of long conditionals or switch statements where you are checking is the action update todo or delete todos)

## 282. First useReducer Example

[Our very own codesandbox example](https://codesandbox.io/s/umres36usereducerusecontext-75ps8?file=/src/App.js)

{type: 'ADD_TODO', task: "Walk the Cat}

TL;DR: useReducer is simply a way of organizing stateful logic into one place (as well as updates to that state)

NOTE: Remember this is just a PATTERN. A PATTERN we will get familiar with.

Example of switch-case with default

```javascript
const reducer = (state, action) => {
  switch (action.type) {
    case "INCREMENT":
      return { count: state.count + action.amount };
    case "DECREMENT":
      return { count: state.count - action.amount };
    case "RESET":
      return { count: 0 };
    default:
      return { count: state.count };
  }
};
```

The whole example

```javascript
import React, { useReducer } from "react";
import "./styles.css";

const reducer = (state, action) => {
  switch (action.type) {
    case "INCREMENT":
      return { count: state.count + action.amount };
    case "DECREMENT":
      return { count: state.count - action.amount };
    case "RESET":
      return { count: 0 };
    default:
      return { count: state.count };
  }
};

// const reducer = (state, action) => {
//   if (action.type === "INCREMENT")
//     return { count: state.count + action.amount };
//   if (action.type === "DECREMENT")
//     return { count: state.count - action.amount };
// };

export default function App() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  return (
    <div className="App">
      <h1>{state.count}</h1>
      <button onClick={() => dispatch({ type: "INCREMENT", amount: 1 })}>
        add one
      </button>
      <button onClick={() => dispatch({ type: "INCREMENT", amount: 5 })}>
        add 5
      </button>
      <button onClick={() => dispatch({ type: "DECREMENT", amount: 1 })}>
        subtract one
      </button>
      <button onClick={() => dispatch({ type: "RESET" })}>RESET</button>
    </div>
  );
}
```

## 283. Defining our Todo Reducer

RANDOM NOTES:
in context
const [todos, dispatch] = useReducer todoResducer, default todos)

update all the files to use {dispatch }
dsf

NOTES FROM NOTES:

1. Create new reducer file
2. Rewrite all of our "add/remove/edit todos" in "reducer" format (switch case)
3. Add useReducer to... files?
4. pdate the places that are calling "add/remove/edit todos" to use "dispatch" and action type
5. profit

## 284. Splitting Into 2 Contexts

THE PROBLEM:
The dispatch is NOT changing
The todos ARE changing

But since they are in the same "Context" every component "consuming" that context (even if it is just consuming `dispatch`, not `todos`) is rerendering.

THE SOLUTION:
Two dispatches!!

ONE FOR TODOS
ONE FOR DISPATCH

NOTE: At the end of this, we will be passing {dispatch} directly instead of creating a new object with dispatch inside it {{ dispatch }} and we will be consuming it similarly, we no longer need to consume it with the {}

NOTES FROM NOTES:

1. Create a `DispatchContext` inside of our other context (so our app only has to require one context)
2. Split our values between the two `Contexts`
3. Change the way we are "consuming" these contexts in the other files -- (import the new context)
   `const dispatch = useContext(DispatchContext);`

```javascript
export const TodoContext = createContext();
export const DispatchContext = createContext();
//...
<TodoContext.Provider value={todos}>
    <DispatchContext.Provider value={dispatch}></DispatchContext.Provider>
    {props.children}
</TodoContext.Provider>
  );
};
```

## 285. Optimizing w/ Memo

PURE COMPONENTS work with CLASS
MEMO works with HOOKS and functional components

Import memo on our TODO
export our todo with memo

## 286. Custom Hook: Reducer + LocalStorage

useLOcalStorageReducer
You can pass a function as a third argument to useReducer
and we now need to do useEffect When state changes

1. Add new hook `useLocalStorageReducer`
2. This hook will be used by `todoContext`
3.
