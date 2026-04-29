# Last updated: 4/29/2026, 11:56:12 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        prefix = [1] * n
5        suffix = [1] * n
6        ans = [1] * n
7
8        for i in range(1, n):
9            prefix[i] = prefix[i-1] * nums[i-1]
10
11        for i in range(n-2, -1, -1):
12            suffix[i] = suffix[i+1] * nums[i+1]
13
14        for i in range(n):
15            ans[i] = prefix[i] * suffix[i]
16
17        return ans