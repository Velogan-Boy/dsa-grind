# Last updated: 5/10/2026, 5:09:15 PM
1class Solution:
2    def maxSubarraySumCircular(self, nums: List[int]) -> int:
3        globMax, globMin = nums[0], nums[0]
4        curMax, curMin = 0, 0
5        total = 0
6        
7        for i, n in enumerate(nums):
8            curMax = max(curMax + n, n)
9            curMin = min(curMin + n, n)
10            total += n
11            globMax = max(curMax, globMax)
12            globMin = min(curMin, globMin)
13
14        return max(globMax, total - globMin) if globMax > 0 else globMax
15