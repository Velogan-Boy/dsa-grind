# Rotate Image

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/rotate-image/submissions/2043108946/
- **Date:** 2026-06-23

## Solution

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for i in range(len(matrix) - 1):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        for i in range(len(matrix)):
            matrix[i].reverse()

         
        
```

---
*Generated automatically by LeetFeedback Extension*
