# Last updated: 5/9/2026, 11:40:03 AM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3
4        n = len(nums)
5        l , r = 0, n - 1
6
7        while l <= r:
8            mid = (l + r) // 2
9
10            if nums[mid] >= target:
11                r = mid - 1
12            else:
13                l = mid + 1
14        
15        return l
16
17        