# Last updated: 3/24/2026, 1:31:47 AM
1class Solution:
2    def maximalRectangle(self, matrix: List[List[str]]) -> int:
3        if not matrix: return 0
4        m = len(matrix[0])
5        heights = [0] * m
6        max_area = 0
7        
8        for row in matrix:
9            for i in range(m):
10                heights[i] = heights[i] + 1 if row[i] == '1' else 0
11            max_area = max(max_area, self.largestRectangleArea(heights))
12        return max_area
13
14    def largestRectangleArea(self, heights: List[int]) -> int:
15        stack = []
16        max_a = 0
17        heights.append(0) # Sentinel to flush stack
18        for i, h in enumerate(heights):
19            while stack and heights[stack[-1]] >= h:
20                height = heights[stack.pop()]
21                width = i if not stack else i - stack[-1] - 1
22                max_a = max(max_a, height * width)
23            stack.append(i)
24        heights.pop()
25        return max_a