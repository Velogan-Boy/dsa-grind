# Last updated: 6/1/2026, 11:34:24 PM
1class Solution:
2    def lengthOfLIS(self, nums):
3        n = len(nums)
4
5        dp = [1] * n
6
7        for i in range(n):
8            for j in range(i):
9                if nums[j] < nums[i]:
10                    dp[i] = max(dp[i], dp[j] + 1)
11
12        return max(dp)