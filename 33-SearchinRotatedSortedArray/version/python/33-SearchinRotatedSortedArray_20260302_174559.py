# Last updated: 3/2/2026, 5:45:59 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        
4        s = 0
5        e = len(nums) - 1
6
7        while s <= e:
8            mid =  (s + e) // 2
9
10            if nums[mid] == target: return mid
11
12            if nums[s] <= nums[mid]:
13                if nums[s] <= target and target <= nums[mid]:
14                    e = mid - 1
15                else:
16                    s = mid + 1
17            else:
18                if nums[mid] <= target and target <= nums[e]:
19                    s = mid + 1
20                else:
21                    e = mid - 1
22            
23        return -1
24
25
26
27