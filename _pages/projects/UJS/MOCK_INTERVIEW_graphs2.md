---
layout: single
title: "UJS: Mock Interview, Graphs II"
tags: UJS mock_interview
permalink: /projects/UJS/mock_interview/graphs2
classes: wide
---

BITMAP 1

```javascript
let bitmap = [
  [0, 0, 0, 0, 0],
  [1, 0, 0, 1, 0],
  [2, 0, 0, 0, 0],
  [1, 1, 1, 0, 2],
];
```

BITMAP 2

```javascript
let bitmap = [
  [0, 0, 0, 0, 0],
  [1, 0, 0, 2, 0],
  [2, 0, 0, 2, 0],
  [1, 1, 1, 2, 2],
];
```

### STARTING HERE

NOTE: Sources does NOT like `const` and `let`

```javascript
var bitmap = [
  [0, 0, 0, 0, 0],
  [1, 0, 0, 2, 0],
  [2, 0, 0, 2, 0],
  [1, 1, 1, 2, 2],
];

function mock_dfs(my_bitmap, colorCode, clickedCoord) {
  var clickedColor = bitmap[clickedCoord[0]][clickedCoord[1]];
  console.log(clickedColor);
  return;
}

var answer = mock_dfs(bitmap, 4, [2, 3]);
```
