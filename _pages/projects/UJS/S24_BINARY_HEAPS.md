---
layout: single
title: "UJS S24: Binary Heaps"
tags: UJS
permalink: /projects/UJS/S24_BINARY_HEAPS/
classes: wide
---

```javascript
class Node {
  constructor(val, priority) {
    this.val = val;
    this.priority = priority;
  }
}

class PQ {
  constructor() {
    this.values = [];
  }

  enqueue(val, priority) {
    const newNode = new Node(val, priority);
    this.values.push(newNode);
    this.bubbleUp();
    console.log("enquing");
  }

  dequeue() {
    const root = values.shift();
    console.log("dequing");
    this.rearrange();
    return root;
  }

  rearrange() {
    console.log("rearranging");
  }
}

myPQ = new PQ();
myPQ.enqueue("Walk cat", 2);
myPQ.enqueue("Brush teeth", 1);
myPQ.enqueue("Load dishwasher", 3);
myPQ.enqueue("Plan meals", 3);
myPQ.enqueue("Read book", 4);
```
