# Last updated: 6/4/2026, 12:01:20 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        
4        n = len(nums)
5        prefix = [1] * n
6        suffix = [1] * n
7
8        for i in range(1, n):
9            prefix[i] = prefix[i - 1] * nums[i-1]
10        
11        for i in range(n - 2 , -1, -1):
12            suffix[i] = suffix[i + 1] * nums[i + 1]
13
14        ans = [1] * n
15
16        for i in range(n):
17            ans[i] = prefix[i] * suffix[i]
18
19        return ans
20
21
22        
23        
24
25
26
27
28        