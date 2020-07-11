---
layout: single
title: "UMRE: Section 33, React Hooks Project"
permalink: /pages/projects/UMRE/section33
tags: UMRE
classes: wide
---

# Section 33: React Hooks Project

## 252. Intro to Hooks Project

## 253. Adding Our Form With Hooks

## 254. Adding Todo Item Component

- GRID from material UI -- center with justify="center"
- GRID from material UI is just like bootstrap

ex:

```javascript
<Grid container justify="center" style={{ marginTop: "1rem" }}>
  <Grid item xs={11} md={8} lg={4}>
    <TodoForm addTodo={addTodo} />
    <TodoList todos={todos} />
  </Grid>
</Grid>
```

\*\*\*\* ADDED @material-ui/icons

## 255. Toggling and Deletion w/ Hooks

- Stateful parent and we pass it down!

* Add RemoveTodo
* Add ToggleTodo
* Add DeleteTodo

\*\*\*\* ADDED uuid

How to toggle with map:

```javascript
const toggleTodo = (todoId) => {
  const updatedTodos = todos.map((todo) =>
    todo.id === todoId ? { ...todo, completed: !todo.completed } : todo
  );
  setTodos(updatedTodos);
};
```

## 256. Editing w/ Hooks

1. Toggle Edit ON and OFF
   useToggle State
   add hook to Todo.js
   isEditing, toggle, useToggleState(false)

2. Make the form
   Then make the form
   EditTodoForm

3. Populate the form
   useInputState()

4. Make the method that will update the that todo when we actually submit

## 257. Small Style Tweaks

1. Add divider back
2. No divider at bottom
3. Margin on left
4. Width of text field
5. Add Autofocus

## 258. LocalStorage w/ UseEffect Hook

1. useEffect()
2. Can send it to local storage `window.localStorage.setItem('todos', JSON.stringify(todos))`
3. for local storageJSON.stringify()
4. localStorage.getItems -- `JSON.parse(window.localStorage.getItem('todos'))`
5. useEffeect runs every rerender, so we should add [todos] as a secondary argument to useEffect
6. Add if else to TodosList

## 259. Refactoring to a Custom Hook

1. Use todo state
2. Move it all over
3. add state
4. add initial value (initialTodosd)
5. Add destructing to Todo.js

## 260. Creating our UseLocaslStorateState Hook

1. Make a new custom hook to use localstorage -- useLocalStorage()
2. Make new file with function and export like normal
3. define function that takes a key and a default value
4. FIRST??make a piece of state based off of value in localstorage
   WE CAN PASS A FUNCTION INTO USE STATE
   we can pass a try/catch into useState
   - let val
   - try (to get from local storage)
   - catch(e) error val = defaultVal
   - MUST RETURN SOMETHING
5. SECOND: use useEffect to update localStorage when state Changes
6. useLocalStorageState in useTodoState
7. getAngry button is goal

NOTES: this is
