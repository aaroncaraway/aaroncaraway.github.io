---
layout: single
title: "CM"
permalink: /pages/CM/shareOptions
tags: CM
classes: wide
---

```javascript
import React from "react";
import { useReducer } from "react";
import "./styles.css";

const reduceShareOptions = (state, action) => {
  if (action.type === "ADD") {
    const clickedValue = state[action.val];
    console.log(clickedValue, state["shareMax"]);
    if (action.val === "shareMin" && clickedValue > state["shareMax"] - 2) {
      return state;
    } else {
      return { ...state, [action.val]: state[action.val] + 1 };
    }
  }
  if (action.type === "SUB") {
    if (state[action.val] !== 0) {
      return { ...state, [action.val]: state[action.val] - 1 };
    }
    return state;
  }
  // if (action.type === "SUB") return { runtime: state.runtime - 1 };
  // if (action.type === "INCREMENT_BY_5") return { runtime: state.runtime + 5 };
};
export default function App() {
  const [state, dispatch] = useReducer(reduceShareOptions, {
    shareMin: 0,
    shareMax: 5,
    shareAllTimes: 1,
    minBetweenLoops: 5,
    shareGroup: 1,
  });
  const runtime =
    state.shareMax * state.shareAllTimes +
    (state.shareAllTimes > 1
      ? state.minBetweenLoops * 60 * state.shareAllTimes
      : 0);
  return (
    <div className="App">
      <h1> RUNTIME (only updates on MAX) IS {runtime} </h1>
      <li>
        {state.shareMin}
        <button onClick={() => dispatch({ type: "SUB", val: "shareMin" })}>
          -
        </button>
        <button onClick={() => dispatch({ type: "ADD", val: "shareMin" })}>
          +
        </button>
      </li>
      <li>
        {state.shareMax}
        <button onClick={() => dispatch({ type: "SUB", val: "shareMax" })}>
          -
        </button>
        <button onClick={() => dispatch({ type: "ADD", val: "shareMax" })}>
          +
        </button>
      </li>
    </div>
  );
}
```
