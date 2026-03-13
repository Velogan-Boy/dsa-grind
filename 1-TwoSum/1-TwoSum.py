# Last updated: 13/03/2026, 23:25:50
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        prevMap = {}  # val -> index
4
5        for i, n in enumerate(nums):
6            diff = target - n
7            if diff in prevMap:
8                return [prevMap[diff], i]
9            prevMap[n] = i
10