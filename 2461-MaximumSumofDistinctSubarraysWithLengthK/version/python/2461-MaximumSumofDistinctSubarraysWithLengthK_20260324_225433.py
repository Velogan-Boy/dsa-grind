# Last updated: 3/24/2026, 10:54:33 PM
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
11            
12            while l <= last_occurrence or r - l + 1 > k:
13                currSum -= nums[l]
14                l += 1
15                
16            hm[nums[r]] = r
17            currSum += nums[r]
18
19            if r - l + 1 == k: ans = max(ans, currSum)
20
21            r += 1
22        return ans