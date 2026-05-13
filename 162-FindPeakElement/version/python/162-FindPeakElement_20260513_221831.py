# Last updated: 5/13/2026, 10:18:31 PM
1class Solution:
2    def findPeakElement(self, nums):
3        n = len(nums)
4
5        if n == 1: return 0
6
7        if nums[0] > nums[1]: return 0
8        if nums[n-1] > nums[n-2]: return n-1
9
10        s,e = 1, n - 2
11
12        while s <= e:
13            mid = (s + e) // 2
14
15            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
16                return mid
17            
18            elif nums[mid] < nums[mid + 1]:
19                s = mid + 1
20            else:
21                e = mid - 1
22
23            