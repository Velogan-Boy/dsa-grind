# Last updated: 5/9/2026, 10:55:21 PM
1class Solution:
2    def trap(self, height):
3
4        l = 0
5        r = len(height) - 1
6
7        leftMax = 0
8        rightMax = 0
9        totalWater = 0
10
11        while l < r:
12
13            leftMax = max(leftMax, height[l])
14            rightMax = max(rightMax, height[r])
15
16            if leftMax < rightMax:
17                totalWater += leftMax - height[l]
18                l += 1
19            else:
20                totalWater += rightMax - height[r]
21                r -= 1
22
23        return totalWater