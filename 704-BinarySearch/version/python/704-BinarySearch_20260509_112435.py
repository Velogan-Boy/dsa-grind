# Last updated: 5/9/2026, 11:24:35 AM
1class Solution(object):
2    def search(self, nums, target):
3        start = 0
4        end = len(nums)-1
5
6        while start <= end:
7            mid = (start + end) // 2
8
9            if nums[mid] == target: return mid
10            elif nums[mid] < target: start = mid + 1
11            else: end = mid - 1
12
13        return -1