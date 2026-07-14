# Last updated: 7/14/2026, 11:40:12 PM
1class Solution:
2    def maximumDifference(self, nums: List[int]) -> int:
3        
4        n = len(nums)
5
6        prefMin = [float("inf")] * n
7
8        for i, num in enumerate(nums):
9            if i == 0: continue
10            prefMin[i] = min(prefMin[i - 1], nums[i - 1])
11
12
13        ans = -1
14        for i, num in enumerate(nums):
15            if prefMin[i] < num:
16                ans = max(ans, num - prefMin[i])
17        
18        return ans
19
20
21
22
23        