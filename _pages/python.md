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

## REMOVE FROM ARRAY

[FROM SO](https://stackoverflow.com/questions/23516212/remove-element-in-list-using-list-comprehension-python)
Simple lst.remove('A') will work:

```python
lst = ['A','B','C']
lst.remove('A')
['B', 'C']
```

However, one call to .remove only removes the first occurrence of 'A' in a list. To remove all 'A' values you can use a loop:

```python
for x in range(lst.count('A')):
    lst.remove('A')
```

If you insist on using list comprehension you can use

```python
[x for x in lst if x != 'A']
['B', 'C']
```

The above will remove all elements equal to 'A'.
