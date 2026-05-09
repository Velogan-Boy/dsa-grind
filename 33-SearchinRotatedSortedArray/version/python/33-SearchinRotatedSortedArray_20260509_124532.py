# Last updated: 5/9/2026, 12:45:32 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3
4        n = len(nums)
5        s, e = 0, n - 1
6
7        while s <= e:
8            mid = (s + e) // 2
9
10            if nums[mid] == target: return mid
11
12            if nums[s] <= nums[mid]:
13                if nums[s] <= target <= nums[mid]:
14                    e = mid - 1
15                else:
16                    s = mid + 1
17            else:
18                if nums[mid] <= target <= nums[e]:
19                    s = mid + 1
20                else:
21                    e = mid - 1
22        
23        return -1
24                
25                
26
27
28     
29
30