# Last updated: 4/1/2026, 11:24:57 PM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3
4        jumps = 0
5        l, r = 0, 0
6        n = len(nums)
7
8        while r < n - 1:
9
10            farthest = 0
11            for i in range(l, r + 1):
12                farthest = max(farthest, i + nums[i])
13            
14            l = r + 1
15            r = farthest
16            jumps+=1
17        
18        return jumps
19
20        