# Last updated: 5/24/2026, 8:00:54 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3
4        @cache
5        def dfs(i):
6            if i < 0: return 0
7
8            pick = dfs(i - 2) + nums[i]
9            notPick = dfs(i - 1)
10
11            return max(pick, notPick)
12
13        return dfs(len(nums) - 1)
14        