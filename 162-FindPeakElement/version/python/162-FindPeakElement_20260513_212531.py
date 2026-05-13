# Last updated: 5/13/2026, 9:25:31 PM
1class Solution:
2    def findPeakElement(self, nums):
3        n = len(nums)
4        low, high = 0, n - 1
5
6        while low < high:
7            mid = (low + high) // 2
8
9            if nums[mid] > nums[mid + 1]:
10                high = mid
11            else:
12                low = mid + 1
13
14        return low