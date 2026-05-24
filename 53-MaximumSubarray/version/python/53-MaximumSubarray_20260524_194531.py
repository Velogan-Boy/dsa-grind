# Last updated: 5/24/2026, 7:45:31 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        currSum = 0
6        maxSum = -inf
7        
8        for num in nums:
9            currSum += num
10            maxSum = max(maxSum, currSum)
11            if currSum < 0: currSum = 0
12        
13        return maxSum
14
15        