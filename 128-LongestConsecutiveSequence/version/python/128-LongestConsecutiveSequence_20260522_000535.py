# Last updated: 5/22/2026, 12:05:35 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        numSet = set(nums)
4        longest = 0
5
6        for num in numSet:
7            if (num - 1) not in numSet:
8                length = 1
9                while (num + length) in numSet:
10                    length += 1
11                longest = max(length, longest)
12        return longest