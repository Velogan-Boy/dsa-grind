# Last updated: 7/12/2026, 6:24:55 PM
class Solution:
    def trap(self, height):
        l = 0
        r = len(height) - 1

        leftMax = 0
        rightMax = 0
        totalWater = 0

        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])

            if leftMax < rightMax:
                totalWater += leftMax - height[l]
                l += 1
            else:
                totalWater += rightMax - height[r]
                r -= 1

        return totalWater