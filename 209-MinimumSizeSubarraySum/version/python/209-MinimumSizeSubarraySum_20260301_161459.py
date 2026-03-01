# Last updated: 3/1/2026, 4:14:59 PM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        left = 0
4        curr_sum = 0
5        ans = float('inf')
6
7        for right in range(len(nums)):
8            curr_sum += nums[right]
9
10            while curr_sum >= target:
11                ans = min(ans, right - left + 1)
12                curr_sum -= nums[left]
13                left += 1
14
15        return 0 if ans == float('inf') else ans