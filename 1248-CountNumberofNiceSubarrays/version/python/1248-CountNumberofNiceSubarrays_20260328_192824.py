# Last updated: 3/28/2026, 7:28:24 PM
1class Solution:
2    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
3
4        def countSubarrys(k):
5            if k < 0: return 0
6
7            n = len(nums)
8            l, r = 0, 0
9            countOdd = 0
10            count = 0
11
12            while r < n:
13                if nums[r] % 2 == 1: 
14                    countOdd += 1
15                
16                while countOdd > k:
17                    if nums[l] % 2 == 1: countOdd -= 1
18                    l+=1
19
20                count += (r - l + 1)
21                r+=1
22            
23            return count
24
25        return countSubarrys(k) - countSubarrys(k - 1)
26
27
28
29
30
31
32
33
34
35
36        