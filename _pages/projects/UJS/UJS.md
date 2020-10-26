---
layout: single
title: "UJS"
tags: UJS
classes: wide
---

## Section 1: Introduction -- DONE

## Section 2: Big O Notation -- DONE

## Section 3: Analyzing Performance of Arrays and Objects -- DONE

## Section 4: Problem Solving Approach -- DONE

## Section 5: Problem Solving Patterns -- DONE

## Section 6: 100% OPTIONAL Challenges -- STARTED

## Section 7: Recursion -- DONE

## Section 8: Recursion Problem Set -- STARTED

## Section 9: Bonus CHALLENGING Recursion Problems -- STARTED

## Section 10: Searching Algorithms -- DONE

## Section 11: Bubble Sort -- STARTED

If we optimize using a "no swap" variable to deal with an almost-sorted list, we have O(N), otherwise we have O(n^2)

## Section 12: Selection Sort

## Section 13: Insertion Sort

## Section 14: Comparing Bubble, Selection, and Insertion

## Sort

## Section 15: Merge Sort

## Section 16: Quick Sort

## Section 17: Radix Sort

## Section 18: Data Structures Introduction -- DONE

## Section 19: Singly Linked Lists -- DONE

## Section 20: Doubly Linked Lists -- DONE

## Section 21: Stacks + Queues -- DONE

## Section 22: Binary Search Trees -- DONE

## Section 23: Tree Traversal -- DONE

## Section 24: Binary Heaps -- STARTED

### Extract Max

Starting ...

THIS HAS INFINITE WHILE LOOP DO NOT RUN

```javascript

    extractMax() {
        const max = this.values[0]
        const end = this.values.pop()
        this.values[0] = end
        this.sinkDown()
        return max;
    }
    sinkDown(){
        let idx = 0;
        const length = this.values.length;
        const element = this.values[0]
        console.log('sinking down')
        while(true) {
            let leftChildIdx = 2 * idx + 1;
            let rightChild = 2 * idx + 2
        }

    }
```

### Building a Priority Queue

WHAT IT IS: A data structure where each element has a priority

Think of it like -- an emergency room queue. Guy with gunshot is going to be treated before scratchy throat

#### NAIVE VERSION:

Use a list to store all elements and iterate over that list to find element with lowest priority

#### NOW, WITH HEAPS!

Time complexity for insertion and deletion: log N

---

Building this with Python

TIL: I do not need the `__str__` method in my Node Class

```python
class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

#     def __str__(self):
#         return [self.val, self.priority]
#         return str(self.val)

class PriorityQueue:
    def __init__(self):
        self.values = []

    def insert(self, val, priority):
        new_node = Node(val, priority)
        self.values.append(new_node)
        self.bubbleUp()

    def extractMin(self):
        min_val = self.values.pop()
        self.sinkDown()

    def bubbleUp(self):
        print('bubbling up')

    def sinkDown(self):
        print('sink down')

    def display(self):
#         print(self.values)
        for i in self.values:
            print(i.val)
```

## Section 25: Hash Tables -- STARTED

## Section 26: Graphs -- STARTED

[Section Notes](https://aaroncaraway.github.io/projects/UJS/S26_GRAPHS)

[Section Notes Test link](/_pages/projects/UJS/S26_GRAPHS.md)

## Section 27: Graph Traversal

## Section 28: Dijkstra's Algorithm!

[GOING BACK TO HEAPS & PRIORITY QUEUES](https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/learn/lecture/8344818#overview)

## Section 29: Dynamic Programming -- STARTED

## Section 30: The Wild West
