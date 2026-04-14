# Last updated: 4/14/2026, 1:19:57 PM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        totalSum = sum(nums)
4        if totalSum % 2 != 0: return False
5        n = len(nums)
6
7        target = totalSum // 2
8
9        memo = [[-1] * (target + 1) for _ in range(n)]
10
11        def dfs(i, target):
12            if memo[i][target] != -1: return memo[i][target]
13
14            if target < 0: return False
15            if target == 0: 
16                memo[i][target] = True
17                return memo[i][target]
18
19            if i < 0: return False
20
21            pick = dfs(i - 1, target - nums[i])
22            notPick = dfs(i - 1, target)
23
24            memo[i][target] =  pick or notPick
25
26            return memo[i][target]
27
28        return dfs(n - 1, target)
29