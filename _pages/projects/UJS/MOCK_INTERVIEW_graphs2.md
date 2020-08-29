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

### SECOND ATTEMPT

THE GOOD:
I did this WITHOUT looking at mock notes from yesterday

THE BAD:
My if/else statements caused me the most pain because I’m dumb and impatient

THE UGLY:
I left my debug statements in there so we can see my awful debugging

```javascript
var bitmap = [
  [0, 0, 0, 0, 0],
  [1, 0, 0, 2, 0],
  [2, 0, 0, 2, 0],
  [1, 1, 1, 2, 2],
];

function mock_dfs(my_bitmap, colorCode, clickedCoord) {
  var r = clickedCoord[0];
  var c = clickedCoord[1];
  var clickedColor = bitmap[r][c];

  function helper(my_bitmap, colorCode, currClickedCoord) {
    console.log("CURR CLICKED COORD", currClickedCoord);
    var r_curr = currClickedCoord[0];
    var c_curr = currClickedCoord[1];
    while (my_bitmap[r_curr][c_curr] !== clickedColor) {
      console.log("not!", my_bitmap[r_curr][c_curr]);
      return;
    }
    my_bitmap[r_curr][c_curr] = colorCode;

    if (r_curr > 0) helper(my_bitmap, colorCode, [r_curr - 1, c_curr]);
    if (r_curr < my_bitmap.length - 1)
      helper(my_bitmap, colorCode, [r_curr + 1, c_curr]);
    if (c_curr > 0) helper(my_bitmap, colorCode, [r_curr, c_curr - 1]);
    if (c_curr < my_bitmap[0].length - 1)
      helper(my_bitmap, colorCode, [r_curr, c_curr + 1]);
  }

  helper(my_bitmap, colorCode, clickedCoord);
  console.log(my_bitmap[3]);
  return my_bitmap;
}

var answer = mock_dfs(bitmap, 4, [2, 3]);
```

### FIRST ATTEMPT

```javascript
var bitmap = [
  [0, 0, 0, 0, 0],
  [1, 0, 0, 2, 0],
  [2, 0, 0, 2, 0],
  [1, 1, 1, 2, 2],
];

function mock_dfs(my_bitmap, colorCode, clickedCoord) {
  var r = clickedCoord[0];
  var c = clickedCoord[1];
  var clickedColor = bitmap[r][c];

  function helper(my_bitmap, colorCode, currClickedCoord) {
    var r_curr = currClickedCoord[0];
    var c_curr = currClickedCoord[1];
    while (my_bitmap[r_curr][c_curr] !== clickedColor) {
      return;
    }
    my_bitmap[r_curr][c_curr] = colorCode;

    if (r_curr >= 0 || r_curr <= len(my_bitmap) - 1)
      helper(my_bitmap, colorCode, [r_curr - 1, c_curr]);
    helper(my_bitmap, colorCode, [r_curr + 1, c_curr]);
    if (c_curr >= 0 || c_curr <= len(my_bitmap) - 1)
      helper(my_bitmap, colorCode, [r_curr, c_curr - 1]);
    helper(my_bitmap, colorCode, [r_curr, c_curr + 1]);
  }

  return my_bitmap;
}

var answer = mock_dfs(bitmap, 4, [2, 3]);
```
