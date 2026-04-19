# Last updated: 4/19/2026, 11:40:33 PM
1class Solution:
2    def lengthOfLIS(self, nums):
3        n = len(nums)
4
5        dp = [[0] * (n + 1) for _ in range(n + 1)]
6
7        for i in range(n - 1, -1, -1):
8            for prev_idx in range(i - 1, -2, -1):
9
10                notPick = dp[i + 1][prev_idx + 1]
11
12                pick = 0
13                if prev_idx == -1 or nums[i] > nums[prev_idx]:
14                    pick = 1 + dp[i + 1][i + 1]
15
16                dp[i][prev_idx + 1] = max(pick, notPick)
17
18        return dp[0][0]