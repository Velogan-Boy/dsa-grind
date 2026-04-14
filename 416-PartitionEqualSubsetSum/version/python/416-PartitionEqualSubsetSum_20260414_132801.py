# Last updated: 4/14/2026, 1:28:01 PM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        totalSum = sum(nums)
4        if totalSum % 2 != 0: return False
5        n = len(nums)
6
7        target = totalSum // 2
8
9        dp = [[False] * (target + 1) for _ in range(n)]
10
11        for i in range(n):
12            dp[i][0] = True
13
14        if nums[0] <= target:
15            dp[0][nums[0]] = True
16        
17        for i in range(1, n):
18            for j in range(1, target + 1):
19                notPick = dp[i - 1][j]
20
21                pick = False
22                if nums[i] <= j:
23                    pick = dp[i - 1][j - nums[i]]
24
25                dp[i][j] = pick or notPick
26
27
28        return dp[n - 1][target]
29