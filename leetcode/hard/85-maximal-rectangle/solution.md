# Maximal Rectangle

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/maximal-rectangle/
- **Date:** 2026-03-23

## Solution

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m = len(matrix[0])
        heights = [0] * m
        max_area = 0
        
        for row in matrix:
            for i in range(m):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_a = 0
        heights.append(0) # Sentinel to flush stack
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_a = max(max_a, height * width)
            stack.append(i)
        heights.pop()
        return max_a
```

---
*Generated automatically by LeetFeedback Extension*
