# Spiral Matrix

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/spiral-matrix/submissions/2000698170/
- **Date:** 2026-05-11

## Solution

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []
        m,n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m - 1, 0, n - 1

        while up <= down and left <= right:
            # left -> right
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up+=1

            # up -> down
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right-=1


            if up <= down:
            # right -> left
                for i in range(right, left - 1, -1):
                    ans.append(matrix[down][i])
                down-=1

            if left <= right:
            # down -> up
                for i in range(down, up - 1, -1):
                    ans.append(matrix[i][left])
                left+=1

        return ans

            




        
```

---
*Generated automatically by LeetFeedback Extension*
