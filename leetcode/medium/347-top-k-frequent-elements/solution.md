# Top K Frequent Elements

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/top-k-frequent-elements/submissions/2009709735/
- **Date:** 2026-05-22

## Solution

```python
import heapq

class Solution:
    """My Own Min-Heap Solution!!!"""
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        occur = {}
        for num in nums:
            occur[num] = occur.get(num, 0) + 1

        heap = []

        for key in occur:
            heapq.heappush(heap, (occur[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]
```

---
*Generated automatically by LeetFeedback Extension*
