# Last updated: 2/27/2026, 10:34:10 PM
1class Solution:
2    def smallestRangeII(self, nums: List[int], k: int) -> int:
3
4        nums.sort()
5
6        minDiff = nums[-1] - nums[0]
7
8        n = len(nums)
9
10        for i in range(n - 1):
11            high = max(nums[-1] - k, nums[i] + k)
12            low = min(nums[0] + k, nums[i + 1] - k)
13
14            minDiff = min(minDiff, high - low)
15
16        return minDiff
17
18
19        