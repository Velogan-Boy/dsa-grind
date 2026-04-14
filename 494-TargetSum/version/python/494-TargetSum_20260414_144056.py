# Last updated: 4/14/2026, 2:40:56 PM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        total = sum(nums)
4
5        if (target + total) % 2 != 0 or abs(target) > total:
6            return 0
7
8        P = (target + total) // 2
9        n = len(nums)
10
11        memo = {}
12
13        def dfs(i, curr_sum):
14            if i == 0:
15                if curr_sum == 0 and nums[0] == 0:
16                    return 2  # +0 and -0
17                if curr_sum == 0 or curr_sum == nums[0]:
18                    return 1
19                return 0
20
21            if (i, curr_sum) in memo:
22                return memo[(i, curr_sum)]
23
24            not_take = dfs(i - 1, curr_sum)
25            take = 0
26            if nums[i] <= curr_sum:
27                take = dfs(i - 1, curr_sum - nums[i])
28
29            memo[(i, curr_sum)] = take + not_take
30            return memo[(i, curr_sum)]
31
32        return dfs(n - 1, P)