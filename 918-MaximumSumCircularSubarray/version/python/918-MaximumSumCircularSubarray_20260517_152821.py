# Last updated: 5/17/2026, 3:28:21 PM
1class Solution:
2    def maxSubarraySumCircular(self, nums: List[int]) -> int:
3        total = sum(nums)
4
5        currMax = globalMax = nums[0]
6        currMin = globalMin = nums[0]
7
8        for num in nums[1:]:
9            currMax = max(num, currMax + num)
10            globalMax = max(globalMax, currMax)
11
12            currMin = min(num, currMin + num)
13            globalMin = min(globalMin, currMin)
14
15        if globalMax < 0:
16            return globalMax
17
18        return max(globalMax, total - globalMin)