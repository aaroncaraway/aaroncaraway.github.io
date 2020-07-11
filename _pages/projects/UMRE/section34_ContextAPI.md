---
layout: single
title: "UMRE: Section 34, Introducing the Context API!"
permalink: /pages/projects/UMRE/section34
tags: UMRE
classes: wide
---

# Section 34: Introducing The Context API!

## 261. Where We Are Heading

- First going to use Context with class based components
- Then going to use Context with functional components
- End goal -- learn about the "redux killer"

## 262. THE CODE FOR THIS SECTION!

## 263. What Even is Context?

- Solves the "problem" of passing state down and down and down for components
- Context probides a solution, it gives us ways of sharing data from one higher level component to other child components further down the tree without having to manually pass props at every single elevel.
- Think of it as a way of creating a store o fdata maybe with some methods that manipulate it

## 264. Adding a Responsive Navbar To Our Context App

- Add Navbar
- Add all from material-ui
- look at `withStyles`
- Add Appbar
  Add toolbar
  Add IcoButton
  Add typography element with className=Classes.title
- Switch for self closing
  add clasName=Pclasses.grow
  glasses.search
  classes.searchIcon

- Add styles/NavBarStyles.js

```javascript
const styles= theme => ({
    root : {
        width: 100%",
        marginBottom:0
    },
    grow: {},
    menuButton: {},
    title: {
        display: "none",
        [theme.breakpoints.up("sm")] : {display: "block"}
    },
    search: { SEE @ 10 MINUTES}
})
```

- NOTE: We can use `backgroundColor: fade(theme.pallette.common.white, 0.15),`
  export styles and import them into `Navbar.js`
- on Navbar js, export default withStyles(styles)(Navbar)

* after render before return add `const {classes} = props.classes

* Input from material UI gives more than just one div

Styles
inputRoot
inputInput

- TRANSITIONS! theme.transitions.create("width") // In english -- "Make me a width transition"

## 265. Adding a Responsive Form to our Context App

- new component form.js
- export withStyles

main -- classes.main

- import styles from styles/From Styles
- FormStyles.js

* Paper
  - Avatar
  - Typography
  - Select
    - MenuItem
    - MenuItem
    - MenuItem
  - htmlform
    - FormControl
      - InputLabel
      - Input
    - FormControl
      - InputLabel
      - Input
    - Form Control Label
    - Button

## 266. Intro to Context and Providers

- Because we don't have root to `html body` we can create our own with 100vh 100vw

PageContent.js
Return a div with styles

- Content is something higher up
  ThemeContext and the components will look up to that one piece of data

- Must create CONTEXTS
  /contexts

ThemeContext.js
import React {createContext}
Call create Context and variable

Now we do a provider
Provder side of things (where we put the state)
Then things can consume it

Every time you get a context, you also get a provider!
This,props.children

TL;DR:

1. Create a context CONTEXT_NAME
2. Create a component (can be named anything, it just returns a rapper using CONTEXT_NAME.Provider, e.g. ThemeContext.Provider)
3. Give that a `value` and then whatever children are inside the wrapper should have access to that information, once we know how to CONSUME it.

#### CONTEXT & PROVIDER

Context & Provider go hand in hand. Provider components add ways that consumer components can subscribe to context changes.

## 267. Consuming A Context

TWO OPTIONS

CONTEXT TYPE
We can set context type and it needs to

IMPORT THE CONTEXT from the page

import {themeContext}
static ContextType=ThemeContext;
"look up the tree and see what context you are in"

## 268. Updating A Context Dynamically

## 269. Writing the Language Context

## 270. Consuming 2 Contexts: Enter the Higher Order Component

MyContext.Consumer
Child is function!?
