# Kth Largest Element in a Stream

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
- **Date:** 2026-04-12

## Solution

```python
class KthLargest:

    def __init__(self, k, nums):
        self.K = k 
        self.pq = [] 

        for num in nums:
            if len(self.pq) < self.K:
                heapq.heappush(self.pq, num)  
            elif num > self.pq[0]:
                heapq.heappop(self.pq)  
                heapq.heappush(self.pq, num)  


    def add(self, val):
        if len(self.pq) < self.K:
            heapq.heappush(self.pq, val)

            return self.pq[0]

        if val > self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq, val)  

        return self.pq[0]  




```

---
*Generated automatically by LeetFeedback Extension*
