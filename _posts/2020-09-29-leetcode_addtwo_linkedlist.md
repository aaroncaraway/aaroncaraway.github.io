---
layout: single
title: "Leetcode 9.28.20"
tags: leetcode
---

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = l1
        curr2 = l2
        prevNode = None
        overflow = 0
        while curr != None:
            print(curr.val)


            new_node = ListNode()

            # curr_sum = curr.val + curr2.val
            new_node.val = curr.val + curr2.val
            new_node.next = prevNode
            prevNode = new_node
            print(new_node)
            curr = curr.next
            curr2 = curr2.next

        # print(curr)

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.

# Add the two numbers and return it as a linked list.

```

```python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = l1
        curr2 = l2
        prevNode = None
        overflow = 0
        while curr != None:
            print(curr.val)


            new_node = ListNode()

            curr_sum = curr.val + curr2.val
            if curr_sum > 9:
                overflow =

            new_node.val = curr.val + curr2.val
            new_node.next = prevNode
            prevNode = new_node
            print(new_node)
            curr = curr.next
            curr2 = curr2.next

        # print(curr)

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.

# Add the two numbers and return it as a linked list.
```
