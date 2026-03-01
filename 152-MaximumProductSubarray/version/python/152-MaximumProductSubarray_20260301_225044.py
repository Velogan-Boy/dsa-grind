# Last updated: 3/1/2026, 10:50:44 PM
1class Solution:
2    def maxProduct(self, nums):
3        ans = nums[0]
4        maxProd = nums[0]
5        minProd = nums[0]
6
7        for i in range(1, len(nums)):
8            curr = nums[i]
9
10            if curr < 0:
11                maxProd, minProd = minProd, maxProd
12
13            maxProd = max(curr, maxProd * curr)
14            minProd = min(curr, minProd * curr)
15
16            ans = max(ans, maxProd)
17
18        return ans
19
20