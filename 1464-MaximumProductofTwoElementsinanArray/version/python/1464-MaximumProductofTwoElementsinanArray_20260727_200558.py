# Last updated: 7/27/2026, 8:05:58 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3
4        n = len(nums)
5        maxValue = 0
6
7        for i in range(n):
8            for j in range(i + 1, n):
9                currProd = (nums[i] - 1) * (nums[j] - 1)
10                maxValue = max(currProd, maxValue)
11            
12        return maxValue
13
14        