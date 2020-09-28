---
layout: single
title: "Leetcode 9.28.20"
tags: leetcode
---

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ids = [n for n in range(len(nums))]
        d = dict(zip(nums,ids))

        for i, num in enumerate(nums):
            diff = target - num
            try:
                other_id = d[diff]
                if i != other_id:
                    return (i, other_id)
            except:
                pass


```

Runtime: 56 ms, faster than 51.79% of Python online submissions for Two Sum.
Memory Usage: 15.9 MB, less than 5.04% of Python online submissions for Two Sum.
