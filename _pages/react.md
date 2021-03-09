---
layout: archive
permalink: /react/
---

[A Visual Guide to State in React](https://daveceddia.com/visual-guide-to-state-in-react/)

With Kent C. Dodds --

1. Intro
2. A UI with Vanilla JS
3. A UI with React
4. Create a UI with React + JSX
5. Use JSX effectively with React
6. Render two elements side-by-side with a fragment
7. Create simple reusable React Compoment
8. Validate Custom React Component Props with proptypes
9. Understand and Use interpolation in JSX
10. Render a React Application
11. Style React Components with ClassName and inline Styles

### NOW, with 30 SECOND SUMMARIES

1. Intro
   1. Best to watch and take notes first
2. A UI with Vanilla JS
   1. Just like we've always done. Create an element in the DOM. use document.CreateElement() to attach that element to the dom.
3. A UI with React
   1. Instead of `document.CreateElement()` we use `React.createElement()`
   2. When we use React.createElement() we can pass props! so `React.createElement('div', {children:['child1','child2'], className:['container]})
4. A UI with React + JSX
   1. We need babble to compile our JSX into javascript
5. Effectively use JSX with React (REWATCH THIS ONE OMG)
   1. you can pass props around with the spread operator `{ ...props}`
6. React Fragments
   1. Lets you put two html elements next to one another
7. Simple Reusable React Component
   1. I can pass a function to React.createElement() simply by making it uppercase
8. Validate Custom React Component Props with PropTypes
   1. import this npm library
   2. It is not included in product
   3. .isRequired() makes the proptype required
   4. Definitely use this to make sure people are using your components correctly
9. Understand and use INTERPOLATION in JSX (ALSO REWATCH OMG)
   1. Everything in {} is going to be EVALUATED. Meaning it can only be an expression -- NOT a function (no for loops etc)
   2. We can remember this by actually envisioning the `React.createElement()` -- we would never pass a for-loop to this, would we?!
10. Rerender a React Application
    1. This was our timer application
11. Style React Components with className and inlineStyles
    1. This was our three differently sized boxes
12. Use Event Handlers with React
    1. We can use `onClick()` and `onFocus()` and `onMouseOver()` and `onBlur()` and `onChange()`
13. Manage State in a React Component with the useState hook
    1. State stores everything in an ARRAY!!! A state array!! So it is essentially `stateArray = React.useState()` and `name = stateArray[0]` and `setName = stateArray[1]`
14. Manage side-effects in a React Component with useEffect hook
    1. This was adding local storage to our form
15. use a lazy Initializer with useState
    1. To avoid unnecessary re-renders with useState, add an arrow function so it ONLY renders when absolutely necessary (the first time, instead of every time state changes)
16. Manage the useEffect dependency Array
    1. Dependency Array! The second parameter we can pass to useEffect to make sure it only runs when that piece of state updates
17. Create reusable custom hooks
    1. useLocalStorageHook()
18. Manipulate the DOM with React refs
    1. VanillaTilt library (mounting and unmounting)
    2. use useEffect() (with an empty dependency array!)
    3. Add a function after to remove it from the dom so we can appropriately garbage collect
19. Understand the React Hook Flow
