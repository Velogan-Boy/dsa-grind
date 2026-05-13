# Last updated: 5/13/2026, 9:40:40 PM
1class Solution:
2    def findPeakElement(self, nums):
3        
4        n = len(nums)
5        for i in range(n):
6            if (i == 0 or nums[i - 1] < nums[i]) and (i == n - 1 or nums[i] > nums[i + 1]):
7                return i
8
9        return 0 