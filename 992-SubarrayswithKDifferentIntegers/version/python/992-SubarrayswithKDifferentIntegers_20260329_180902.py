# Last updated: 3/29/2026, 6:09:02 PM
1class Solution:
2    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
3        def kDistinctChar(myK):
4            if myK < 0: return 0
5
6            l,r = 0,0 
7            n = len(nums)
8            hm = {}
9            count = 0
10
11            while r < n:
12                hm[nums[r]] = hm.get(nums[r], 0) + 1
13
14                while len(hm) > myK:
15                    hm[nums[l]] -= 1
16                    if hm[nums[l]] == 0: del hm[nums[l]]
17                    l += 1
18
19                count += r - l + 1
20                r+= 1
21            
22            return count
23
24        return  kDistinctChar(k) - kDistinctChar(k - 1) 
25
26    
27        