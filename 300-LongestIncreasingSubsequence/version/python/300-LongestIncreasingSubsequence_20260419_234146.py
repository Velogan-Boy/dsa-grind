# Last updated: 4/19/2026, 11:41:46 PM
1class Solution:
2    def lengthOfLIS(self, nums):
3        n = len(nums)
4
5        nextRow = [0] * (n + 1)
6
7        for i in range(n - 1, -1, -1):
8            curr = [0] * (n + 1)
9
10            for prev_idx in range(i - 1, -2, -1):
11
12                notPick = nextRow[prev_idx + 1]
13
14                pick = 0
15                if prev_idx == -1 or nums[i] > nums[prev_idx]:
16                    pick = 1 + nextRow[i + 1]
17
18                curr[prev_idx + 1] = max(pick, notPick)
19
20            nextRow = curr
21
22        return nextRow[0]