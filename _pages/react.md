---
layout: archive
permalink: /react/
---

[A Visual Guide to State in React](https://daveceddia.com/visual-guide-to-state-in-react/)

With Kent C. Dodds --

1. Intro
2. A UI with Vanilla JS
3. A UI with React

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
