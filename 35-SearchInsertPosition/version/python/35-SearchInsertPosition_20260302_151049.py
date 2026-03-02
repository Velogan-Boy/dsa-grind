# Last updated: 3/2/2026, 3:10:49 PM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3
4        s = 0
5        e = len(nums) - 1
6
7        while s <= e:
8            mid = (s + e) // 2
9
10            if nums[mid] == target:
11                return mid
12            elif nums[mid] > target:
13                e = mid - 1
14            else:
15                s = mid + 1
16        
17        return s
18        