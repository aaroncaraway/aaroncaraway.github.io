---
layout: single
title: "UJS S27: Graph Traversal"
tags: UJS
permalink: /projects/UJS/S27_GRAPHS/
classes: wide
---

TRAVERSAL: Visiting every single node and graph

Real world: nearest neighbors is more common

We have no ROOT, we need to specify a starting point

### Graph Traversal Uses

- Peer to peer networking
- web crawlers
- finding closest matches or recommendations
- shortest path problems
  - GPS nav
  - Solving Mazes
  - AI (shortest path to win the game)

DEPTH FIRST --> Prioritize children
In a graph, DEPTH FIRST simply means moving away from the root

### DFS RECURSIVE

Python I did it outside the class

```python
result = []
visited = {}

def helper(vertex):
    print(vertex)
    if not vertex:
        return

    visited[vertex] = True
    result.append(vertex)

    for item in g.adjacencyList[vertex]:
        if item not in visited:
            helper(item)

helper('A')

```

javascript inside the class

```javascript
    depthFirstSearch(start) {
        const result = []
        const visited = {}
        const adjacencyList = this.adjacencyList;

        (function dfs(vertex){
            if(!vertex) return null
            visited[vertex] = true
            result.push(vertex)
            adjacencyList[vertex].forEach(neighbor => {
                if(!visited[neighbor]){
                    return dfs(neighbor)
                }
            })
        })(start);

        return result;
    }
```
