# Pascal's Triangle

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/pascals-triangle/submissions/1967096573/
- **Date:** 2026-04-02

## Solution

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            currRow = [0] * (i + 1)

            for j in range(i + 1):
                if j == 0 or j == i:
                    currRow[j] = 1
                else:
                    currRow[j] = ans[i - 1][j - 1] + ans[i - 1][j]
            
            ans.append(currRow)

        return ans



        
```

---
*Generated automatically by LeetFeedback Extension*
