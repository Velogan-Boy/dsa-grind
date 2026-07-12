# Stone Game

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/stone-game/submissions/2065046073/
- **Date:** 2026-07-12

## Solution

```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        # max advantage i can have over other player in the subarry piles[l, r]
        @cache
        def dfs(l, r): 
            if l == r: return piles[l]

            pickStart = piles[l] - dfs(l+1,r)
            pickEnd = piles[r] - dfs(l, r-1)

            return max(pickStart, pickEnd)

        return dfs(0, len(piles) - 1) >= 1

        
```

---
*Generated automatically by LeetFeedback Extension*
