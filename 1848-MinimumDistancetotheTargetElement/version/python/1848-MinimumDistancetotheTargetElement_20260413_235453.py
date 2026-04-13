# Last updated: 4/13/2026, 11:54:53 PM
1class Solution:
2    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
3
4        mini = inf
5        for i, num in enumerate(nums):
6            if num == target:
7                mini = min(abs(start - i), mini)
8
9        return mini
10
11        