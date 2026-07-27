# Last updated: 7/27/2026, 9:28:06 PM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4
5        @cache
6        def dfs(i, currSum):
7            if i == n: return 1 if currSum == target else 0
8
9            return dfs(i + 1, currSum - nums[i]) + dfs(i + 1, currSum + nums[i])
10
11        return dfs(0, 0)
12
13        