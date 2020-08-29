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

Depth first ITERATIVELY involves pushing onto a stack.

Additionally, we figured out how to actually step through code using the chrome debugger!!
(Highlight the line to run and do the run key command)

### DFS Iterative V1 (my attempt without watching him first)

```javascript
    depthFirstSearch_iterative(start){
        let todo = [start]
        let visited = {}
        let result = []
        let current;
        let neighbors;
        while (todo.length !== 0) {
            console.log(todo)
            current = todo.pop()
            if (!visited[current]){
                visited[current] = true

                result.push(current)
            }
            neighbors = this.adjacencyList[current]
            for (let i = 0; i < neighbors.length; i++){
                const neighbor = neighbors[i]
                if (!visited[neighbor]){
                    console.log(neighbors[i])
                    todo.push(neighbors[i])
                }
            }

        }
        console.log('RESULT', result)
        return result
    }

```

### DFS Iterative V2 (also no looking, but after video)

```javascript
       depthFirstSearch_iterative(start){
           let stack = [start]
           let visited = {}
           let results = [start]
           let current;

           visited[start] = true
           while(stack.length){
                current = stack.pop()
                this.adjacencyList[current].forEach((vert) => {
                    if(visited[vert]) {console.log('visited!')}
                    else {
                        visited[vert] = true
                        results.push(vert)
                        stack.push(vert)
                    }
                    console.log(vert)
                })
           }
           return results
       }

```

### DFS Iterative V3 (after video again)

```javascript
// V3 After watching video again
           depthFirstSearch_iterative(start) {
               let stack = [start]
               let results = []
               let visited = {}
               let current;

                visited[start] = true
//                while there is still something in the stack
               while(stack.length){
//                    pop off what's in the stack and get his/her neighbors
                    current = stack.pop()
                    results.push(current)

                    this.adjacencyList[current].forEach(neighbor => {
//                         if the neighbor has not been visited, visit and add their neighbors
                        if(!visited[neighbor]){
                            visited[neighbor] = true
                            stack.push(neighbor)
                        }
                    })
               }
               return results
           }
```

### BFS (attempt on 8/29/20)

```javascript
    bfs(start) {
//         remove from front of queue with queue.shift()
        var queue = [start]
        var results = []
        var visited = {}
        var current;
        var neighbors;

//         visited[start] = true
        while(queue.length){
            current = queue.shift()
            if(!visited[current]){
                visited[current] = true
                results.push(current)
                neighbors = this.adjacencyList[current]
                neighbors.forEach((neighbor) => {
                    if(!visited[neighbor]){
                        queue.push(neighbor)
                        console.log(current, queue)
                    }
                })

            }

        }
        return results


    }

```
