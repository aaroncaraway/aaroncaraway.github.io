---
layout: single
title: "UJS S26: Graphs"
tags: UJS
permalink: /projects/UJS/S26_GRAPHS/
classes: wide
---

## 206. PREREQUISITES

## 207. Intro to Graphs

## 208. Uses for Graphs

## 209. Types of Graphs

## 210. Storing Graphs: Adjacency Matrix

## 211. Storing Graphs: Adjacency List

## 212. Adjacency Matrix Vs. List BIG O

#### ADJACENCY LIST:

PRO:

- takes up less space if data is sparse
- faster to iterate over all edges

CON:

- can be slow to look up specific edges

#### ADJACENCY MATRIX:

PRO:

- faster to look up specific edge

CON:

- Takes up more space if data is sparse
- Slower to iterate over all edges

### WITH BIG O:

#### ADJACENCY LIST:

#### ADJACENCY MATRIX:

## 213. Add Vertex Intro

```javascript
class Graph {
  constructor() {
    this.adjacencyList = {};
  }

  addVertex(val) {
    //  SIMPLE
    //  this.adjacencyList[val] = [];
    // With error handling
    if (!this.adjacencyList[val]) this.adjacencyList[val] = [];
  }

  printMe() {
    for (let property in this.adjacencyList) {
      console.log(property, this.adjacencyList[property]);
    }
  }
}

myGraph = new Graph();
myGraph.addVertex("Tokyo");
myGraph.printMe();
```

```python
class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, val):
        self.adjacencyList[val] = []

    def print_me(self):
        for k,v in self.adjacencyList.items():
            print(k,v)

myGraph = Graph()
myGraph.addVertex('Tokyo')
myGraph.print_me()
```

## 214. Add Vertex Solution

## 215. Add Edge Intro

## 216. Add Edge Solution

```python
class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, val):
        self.adjacencyList[val] = []

    def addEdge(self, vert1, vert2):
#         self.adjacencyList[vert1] = self.adjacencyList[vert1] + [vert2]
#         self.adjacencyList[vert2] = self.adjacencyList[vert2] + [vert1]
#         self.adjacencyList[vert1] += [vert2]
#         self.adjacencyList[vert2] += [vert1]
        self.adjacencyList[vert1].append(vert2)
        self.adjacencyList[vert2].append(vert1)

    def removeEdge(self, vert1, vert2):
        self.adjacencyList[vert1] = [item for item in self.adjacencyList[vert1] if item != vert2]
        self.adjacencyList[vert2] = [item for item in self.adjacencyList[vert2] if item != vert1]

    def print_me(self):
        for k,v in self.adjacencyList.items():
            print(k,v)

```

```javascript
class Graph {
  constructor() {
    this.adjacencyList = {};
  }

  addVertex(val) {
    if (!this.adjacencyList[val]) this.adjacencyList[val] = [];
  }

  addEdge(vert1, vert2) {
    this.adjacencyList[vert1].push(vert2);
    this.adjacencyList[vert2].push(vert1);
  }

  removeEdge(vert1, vert2) {
    this.adjacencyList[vert1] = this.adjacencyList[vert1].filter(
      (item) => item !== vert2
    );
    this.adjacencyList[vert2] = this.adjacencyList[vert2].filter(
      (item) => item !== vert1
    );
  }

  printMe() {
    for (let property in this.adjacencyList) {
      console.log(property, this.adjacencyList[property]);
    }
  }
}

myGraph = new Graph();
myGraph.addVertex("Tokyo");
myGraph.addVertex("LA");
myGraph.addVertex("CO");
myGraph.addEdge("Tokyo", "LA");
myGraph.addEdge("LA", "CO");
myGraph.printMe();

myGraph.removeEdge("Tokyo", "LA");
myGraph.printMe();
```

## 217. Remove Edge Intro

## 218. Remove Edge Solution

## 219. Remove Vertex Intro

## 220. Remove Vertex Solution
