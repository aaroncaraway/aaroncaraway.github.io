---
layout: single
title: UMRR Notes"
permalink: /UMRR/
---


## Section 1: Let's Dive In!

### 10. Javascript Module Systems

1. Make new cra
2. delete everything from src
3. make new index.html
   1. import React and ReactDOM libraries
   2. create a react component
   3. Take the react component and show it on the screen

## Section 2: Building Content with JSX

## Section 3: Communicating with Props

## Section 4: Structuring Apps with Class-Based Components

## Section 5: State in React Components

```javascript

import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {lat: null, errorMessage: null}

    window.navigator.geolocation.getCurrentPosition(
      // success callback
      position => this.setState({ lat: position.coords.latitude }),
      // error callback
      err => this.setState({ errorMessage: err.message})
    )
  }
  render(){

      if (this.state.errorMessage && !this.state.lat) {
        return(<div> Latitude: {this.state.errorMessage} </div>)
      }

      if (!this.state.errorMessage && this.state.lat) {
        return(<div> Error: {this.state.lat} </div>)
      }

      
      return(<div> Loading! </div>)
      
  }
}

ReactDOM.render(<App />, document.querySelector("#root"))

```

### THREE THINGS:

Lifecycle methods!
Component re-renders when state is updated

1. ComponentDidMount (runs once, when component is MOUNTED onto the dom)
2. ComponentDidUpdate (runs once component re-renders **** AFTER STATE HAS BEEN UPDATED!!)
3. ComponentWillUnMount

## Section 6: Understanding Lifecycle Methods

### 61:

GOAL: Move code from constructor to ComponentDidMount

### 62:


## Section 7: Handling User Input with Forms and Events

## Section 8: Making API Requests with React

## Section 9: Building Lists of Records

## Section 10: Using Ref's for DOM Access

## Section 11: Let's Test Your React Mastery!

## Section 12: Understanding Hooks in React

## Section 13: Navigation From Scratch

## Section 14: Hooks in Practice

## Section 15: Deploying a React App

## Section 16: On We Go...To Redux!

## Section 17: Integrating React with Redux

## Section 18: Async Actions with Redux Thunk

## Section 19: Redux Store Design

## Section 20: Navigation with React Router

## Section 21: Handling Authentication with React

## Section 22: Redux Dev Tools

## Section 23: Handling Forms with Redux Form

## Section 24: REST-Based React Apps

## Section 25: Using React Portals

## Section 26: Implementing Streaming Video

## Section 27: The Context System with React

## Section 28: Replacing Redux with Context

## Section 29: Working with Older Versions of React

## Section 30: Ajax Requests with React

## Section 31: Modeling Application State

## Section 32: Managing App State with Redux

## Section 33: Intermediate Redux: Middleware

## Section 34: React Router + Redux Form v6

## Section 35: Bonus Topics

## Section 36: React Router + Redux Form v4

## Section 37: Extras