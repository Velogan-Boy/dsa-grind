# Last updated: 7/7/2026, 12:13:34 AM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        s = 0
4        e = len(nums) - 1
5        ans = inf
6
7        while s <= e:
8            mid = (s + e) // 2
9
10            if nums[s] <= nums[mid]:
11                ans = min(ans,nums[s])
12                s = mid + 1
13            else:
14                ans = min(ans,nums[mid])
15                e = mid - 1
16        
17        return ans if ans != inf else -1
18
19
20        