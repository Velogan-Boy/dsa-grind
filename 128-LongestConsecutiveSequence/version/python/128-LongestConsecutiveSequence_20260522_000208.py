# Last updated: 5/22/2026, 12:02:08 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        if not nums: return 0
4        nums.sort()
5
6        longest = 1
7        currLength = 1
8        prev = nums[0]
9
10        for i in range(1, len(nums)):
11            if nums[i] == prev + 1:
12                currLength += 1
13            elif nums[i] == prev:
14                pass
15            else:
16                currLength = 1
17
18            prev = nums[i]
19            longest = max(longest, currLength)
20
21        return longest
22
23
24
25
26
27