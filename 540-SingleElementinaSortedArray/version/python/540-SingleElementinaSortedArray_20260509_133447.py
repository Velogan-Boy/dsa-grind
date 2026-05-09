# Last updated: 5/9/2026, 1:34:47 PM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        n = len(nums)
4        low, high = 0, n - 1
5
6        while low <= high:
7            mid = (low + high) // 2
8
9            left_same = (mid > 0 and nums[mid] == nums[mid - 1])
10            right_same = (mid < n - 1 and nums[mid] == nums[mid + 1])
11
12            if not left_same and not right_same:
13                return nums[mid]
14
15            if (mid % 2 == 1 and left_same) or (mid % 2 == 0 and right_same):
16                low = mid + 1
17            else:
18                high = mid - 1
19
20        return -1
21
22