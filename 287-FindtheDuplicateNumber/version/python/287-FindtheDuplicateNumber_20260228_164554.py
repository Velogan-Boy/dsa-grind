# Last updated: 2/28/2026, 4:45:54 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3
4        for i in range(len(nums)):
5            idx = abs(nums[i])
6            if nums[idx] < 0:
7                return idx
8
9            nums[idx] = -nums[idx] 
10
11        return 0
12        