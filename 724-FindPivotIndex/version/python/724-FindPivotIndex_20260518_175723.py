# Last updated: 5/18/2026, 5:57:23 PM
1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        totalSum = sum(nums)
6        leftSum = 0
7
8        for i in range(n):
9            if leftSum * 2 == totalSum - nums[i]:
10                return i
11            
12            leftSum += nums[i]
13
14        return -1
15
16
17
18        