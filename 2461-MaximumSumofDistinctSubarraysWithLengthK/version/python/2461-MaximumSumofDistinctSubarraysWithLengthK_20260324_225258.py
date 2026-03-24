# Last updated: 3/24/2026, 10:52:58 PM
1class Solution:
2    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
3        ans = 0
4        currSum = 0
5        l = 0
6        r = 0
7        hm = {}
8
9        while r < len(nums):
10            last_occurrence = hm.get(nums[r], -1)
11            while l <= last_occurrence or r - l + 1 > k:
12                currSum -= nums[l]
13                l += 1
14            hm[nums[r]] = r
15            currSum += nums[r]
16            if r - l + 1 == k:
17                ans = max(ans, currSum)
18            r += 1
19        return ans