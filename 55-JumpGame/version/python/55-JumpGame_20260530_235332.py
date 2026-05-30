# Last updated: 5/30/2026, 11:53:32 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        maxIndex = 0
4
5        for i in range(len(nums)):
6            if i > maxIndex: return False
7            maxIndex = max(i + nums[i], maxIndex)
8
9
10        return True
11
12        