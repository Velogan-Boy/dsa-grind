# Last updated: 7/6/2026, 7:23:37 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4        
5        @cache
6        def dfs(i):
7
8            if i >= n: return 0
9
10            rob = dfs(i + 2) + nums[i]
11            notRob = dfs(i + 1) + 0
12
13            return max(rob, notRob) 
14
15        return dfs(0)
16
17
18        