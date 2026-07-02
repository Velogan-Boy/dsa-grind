# Last updated: 7/2/2026, 11:40:18 PM
1class Solution:
2    def trap(self, height):
3        l = 0
4        r = len(height) - 1
5
6        leftMax = 0
7        rightMax = 0
8        totalWater = 0
9
10        while l < r:
11            leftMax = max(leftMax, height[l])
12            rightMax = max(rightMax, height[r])
13
14            if leftMax < rightMax:
15                totalWater += leftMax - height[l]
16                l += 1
17            else:
18                totalWater += rightMax - height[r]
19                r -= 1
20
21        return totalWater