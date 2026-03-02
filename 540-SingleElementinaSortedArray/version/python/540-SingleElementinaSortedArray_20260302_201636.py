# Last updated: 3/2/2026, 8:16:36 PM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        left, right = 0, len(nums) - 1
4        while left < right:
5            mid = (left + right) // 2
6            if mid % 2 == 1:
7                mid -= 1
8            if nums[mid] != nums[mid + 1]:
9                right = mid
10            else:
11                left = mid + 2
12        return nums[left]