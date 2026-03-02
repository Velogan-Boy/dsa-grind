# Last updated: 3/2/2026, 5:43:54 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        
4        s = 0
5        e = len(nums) - 1
6
7
8        while s <= e:
9            mid =  (s + e) // 2
10
11            if nums[mid] == target: return mid
12
13            if nums[s] <= nums[mid]:
14                if nums[s] <= target and target <= nums[mid]:
15                    e = mid - 1
16                else:
17                    s = mid + 1
18            else:
19                if nums[mid] <= target and target <= nums[e]:
20                    s = mid + 1
21                else:
22                    e = mid - 1
23            
24        return -1
25
26
27
28