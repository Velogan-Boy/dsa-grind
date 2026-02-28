# Last updated: 2/28/2026, 4:34:54 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3
4        if not nums: return 0
5
6        nums.sort()
7
8        longest = 1
9        curr = 1
10        prev = inf
11
12        for i in range(len(nums)):
13            if nums[i] == prev + 1:
14                curr+=1
15            elif nums[i] == prev:
16                pass
17            else:
18                curr = 1
19
20            prev = nums[i]
21            longest = max(longest, curr)
22
23        return longest
24
25
26
27
28