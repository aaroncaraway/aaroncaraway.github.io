---
layout: archive
permalink: /python/
---

## Adding to Dictionary

```python
    def addEdge(self, vert1, vert2):
#         self.adjacencyList[vert1] = self.adjacencyList[vert1] + [vert2]
#         self.adjacencyList[vert2] = self.adjacencyList[vert2] + [vert1]
#         self.adjacencyList[vert1] += [vert2]
#         self.adjacencyList[vert2] += [vert1]
        self.adjacencyList[vert1].append(vert2)
        self.adjacencyList[vert2].append(vert1)

```

```javascript
  addEdge(vert1, vert2) {
    this.adjacencyList[vert1].push(vert2);
    this.adjacencyList[vert2].push(vert1);
  }
```
