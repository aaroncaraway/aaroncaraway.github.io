---
layout: single
title: 'ATBS CH3'
tags: ATBS
classes: wide
---

```python
def collatz(number):
    if number % 2 == 0:
        return(number // 2)
    else:
        return(3*number+1)

print('Starting input')
result = int(input())

while(result != 1):
    print(result)
    result = collatz(result)

```