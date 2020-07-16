---
layout: single
title: "UMRE: Solo Project Attempt"
permalink: /pages/projects/UMRE/section36
tags: UMRE react movies
classes: wide
---

```console
npx create-react-app umre-movies
cd umre-movies
rm public/favicon.ico public/logo192.png public/logo512.png
rm src/App.test.js src/logo.svg src/serviceWorker.js src/setupTests.js src/index.css
```

- App
  - MovieApp
    - MovieList

```javascript
import React from "react";
import "./App.css";
import MovieApp from "./MovieApp";

function App() {
  return (
    <div className="App">
      <MovieApp />
    </div>
  );
}

export default App;
```
