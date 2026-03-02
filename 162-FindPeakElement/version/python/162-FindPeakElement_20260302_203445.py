# Last updated: 3/2/2026, 8:34:45 PM
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        l, r = 0, len(nums) - 1
4        while l < r:
5            mid = (l + r) // 2
6            if nums[mid] > nums[mid + 1]:
7                r = mid
8            else:
9                l = mid + 1
10        return l