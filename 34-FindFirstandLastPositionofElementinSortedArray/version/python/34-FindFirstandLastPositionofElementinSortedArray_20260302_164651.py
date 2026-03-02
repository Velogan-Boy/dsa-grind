# Last updated: 3/2/2026, 4:46:51 PM
1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        s = self.binarySearch(nums,target, True)
4        e = self.binarySearch(nums,target, False)
5
6        return [s, e]
7
8    def binarySearch(self, nums: List[int], target: int, firstOccurence: bool) -> int:
9        l, h = 0, len(nums)-1
10        ans = -1
11
12        while l <= h:
13            mid = (l + h) // 2
14            if nums[mid] > target: h = mid - 1
15            elif nums[mid] < target: l = mid + 1
16            else:
17                ans = mid
18
19                if firstOccurence: h = mid - 1
20                else: l = mid + 1
21
22                
23
24        
25        return ans
26
27
28        