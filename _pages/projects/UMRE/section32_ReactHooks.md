---
layout: single
title: "UMRE: Section 32, Introducing React Hooks"
permalink: /pages/projects/UMRE/section32
tags: UMRE
classes: wide
---

# Section 32: Introducing React Hooks

## 247. Intro to Hooks & useState

[SANDBOX](https://codesandbox.io/s/umres32247-s3zdu)

### NOTES

- Called "Hooks" because we are "Hooking into" state

* Hooks are new, classes will not leave forever
* Easier to reuse
* Ships with a few hooks

- `useState`

* We call `useState` and give in an initial value
* It returns two things -- a reference to that piece of state, a function that will change that piece of state

## 248. Building a Custom Hook: useToggleState

### NOTES:

- It is conventional to start hooks with `use` so `useToggle`

```javascript
function Toggler() {
  const [isHappy, setIsHappy] = useState(true);
  return <h1 onClick={() => setIsHappy(!isHappy)}> {isHappy ? ":)" : ":("}</h1>;
}

export default Toggler;
```

### Instead of THIS

```javascript
function Toggler() {
  const [isHappy, setIsHappy] = useState(true);
  const [isHeartbroken, setIsHeartbroken] = useState(false);
  const toggleIsHappy = () => {
    setIsHappy(!isHappy);
  };
  const toggleIsHeartbroken = () => {
    setIsHeartbroken(!isHeartbroken);
  };
  return (
    <div>
      <h1 onClick={toggleIsHappy}> {isHappy ? ":)" : ":("}</h1>
      <h1 onClick={toggleIsHeartbroken}> {isHeartbroken ? "</3" : "<3"}</h1>
    </div>
  );
}
```

### DO THIS!!

#### 1. Add a custom `useToggle` hook

_NEW FILE_ **hooks/useToggle**

```javascript
import { useState } from "react";

function useToggle(initialVal = false) {
  const [state, setState] = useState(initialVal);

  const toggle = () => {
    setState(!state);
  };
  return [state, toggle];
}

export default useToggle;
```

_UPDATES TO ORIGINAL FILE_

```javascript
import useToggle from "./hooks/useToggle";

function Toggler() {
  const [isHappy, toggleIsHappy] = useToggle(true);
  const [isHeartbroken, toggleIsHeartbroken] = useToggle(false);

  return (
    <div>
      <h1 onClick={toggleIsHappy}> {isHappy ? ":)" : ":("}</h1>
      <h1 onClick={toggleIsHeartbroken}> {isHeartbroken ? "</3" : "<3"}</h1>
    </div>
  );
}
export default Toggler;
```

## 249. Building a Custom Hook: useInputState

## 250. The useEffect Hook

## 251. Fetching Data w/ the useEffect Hook
