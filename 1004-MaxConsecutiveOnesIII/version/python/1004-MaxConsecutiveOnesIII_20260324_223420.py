# Last updated: 3/24/2026, 10:34:20 PM
1class Solution:
2    def longestOnes(self, nums, k):
3        l, r = 0, 0
4        n = len(nums)
5        ans = 0
6        zeroes = 0
7
8        while r < n:
9            if nums[r] == 0: zeroes+=1
10
11            while zeroes > k:
12                if nums[l] == 0: zeroes-=1
13                l+=1
14
15            ans = max(ans, r - l + 1)
16            r+=1
17
18        return ans
19
20
21
22            
23            
24
25                