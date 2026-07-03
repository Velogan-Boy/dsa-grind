# Last updated: 7/3/2026, 11:42:05 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3
4        maxArea = 0
5
6        l,r = 0, len(height) - 1
7
8        while l < r:
9            maxArea = max(maxArea, (r - l) * min(height[l], height[r]))
10
11            if height[l] > height[r]: r-=1
12            else: l +=1
13
14        return maxArea
15
16        