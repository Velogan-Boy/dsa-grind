# Top K Frequent Elements

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/top-k-frequent-elements/submissions/2008364699/
- **Date:** 2026-05-20

## Solution

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        sortedNums = sorted(freq.keys(), key = lambda x: freq[x], reverse=True)

        return sortedNums[:k]



        

```

---
*Generated automatically by LeetFeedback Extension*
