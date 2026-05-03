# Last updated: 5/3/2026, 5:36:46 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        
4        i = 0
5        j = 0
6
7        while j < len(nums):
8            if nums[j] != 0:
9                nums[i] = nums[j]
10                i+=1
11            
12            j+=1
13
14        while i < len(nums):
15            nums[i] = 0
16            i+=1
17        
18        