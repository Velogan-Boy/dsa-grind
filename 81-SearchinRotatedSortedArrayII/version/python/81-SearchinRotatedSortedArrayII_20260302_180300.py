# Last updated: 3/2/2026, 6:03:00 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> bool:
3        
4        s = 0
5        e = len(nums) - 1
6
7        while s <= e:
8            mid =  (s + e) // 2
9
10            if nums[mid] == target: return True
11
12            if nums[s] == nums[mid] == nums[e]: 
13                s+=1
14                e-=1
15                continue
16
17            if nums[s] <= nums[mid]:
18                if nums[s] <= target and target <= nums[mid]:
19                    e = mid - 1
20                else:
21                    s = mid + 1
22            else:
23                if nums[mid] <= target and target <= nums[e]:
24                    s = mid + 1
25                else:
26                    e = mid - 1
27            
28        return False
29
30
31
32