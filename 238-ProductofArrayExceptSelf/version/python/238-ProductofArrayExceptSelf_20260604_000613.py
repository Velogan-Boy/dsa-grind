# Last updated: 6/4/2026, 12:06:13 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        
4        n = len(nums)
5        ans = [1] * n
6
7        for i in range(1, n):
8            ans[i] = ans[i - 1] * nums[i - 1]
9        
10        suffix = nums[n - 1]
11        for i in range(n - 2 , -1, -1):
12            ans[i] *= suffix
13            suffix *= nums[i]
14
15        return ans
16
17
18        
19        
20
21
22
23
24        