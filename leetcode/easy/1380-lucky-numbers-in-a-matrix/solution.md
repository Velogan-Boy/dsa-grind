# Lucky Numbers in a Matrix

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/lucky-numbers-in-a-matrix/
- **Date:** 2026-07-12

## Solution

```python
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])

        min_row = set()
        max_col = set()

        for i in range(m):
            mini = float('inf')

            for j in range(n):
                if mini > matrix[i][j]:
                    mini = matrix[i][j]
            
            min_row.add(mini)
        
        for j in range(n):
            maxi = float('-inf')

            for i in range(m):
                if maxi < matrix[i][j]:
                    maxi = matrix[i][j]
                
            max_col.add(maxi)

        return list(min_row & max_col)



        
```

---
*Generated automatically by LeetFeedback Extension*
