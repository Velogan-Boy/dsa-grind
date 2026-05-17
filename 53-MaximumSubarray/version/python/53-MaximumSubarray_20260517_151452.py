# Last updated: 5/17/2026, 3:14:52 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        currSum = 0
6        maxSum = -inf
7        for num in nums:
8            currSum += num
9            maxSum = max(maxSum, currSum)
10            if currSum < 0: currSum = 0
11        
12        return maxSum
13
14        