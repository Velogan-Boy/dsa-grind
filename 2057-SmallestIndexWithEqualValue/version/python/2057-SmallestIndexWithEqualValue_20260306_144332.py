# Last updated: 3/6/2026, 2:43:32 PM
1class Solution:
2    def smallestEqual(self, nums: List[int]) -> int:
3        for i in range(len(nums)):
4            if i % 10 == nums[i]:
5                return i
6        
7        return -1
8        