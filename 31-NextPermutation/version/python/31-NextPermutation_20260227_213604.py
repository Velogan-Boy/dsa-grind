# Last updated: 2/27/2026, 9:36:04 PM
1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        n = len(nums)
4        i = n - 2
5        
6        while i >= 0 and nums[i] >= nums[i + 1]:
7            i -= 1
8        
9        if i >= 0:
10            j = n - 1
11            while nums[j] <= nums[i]:
12                j -= 1
13     
14            nums[i], nums[j] = nums[j], nums[i]
15        
16        nums[i + 1:] = reversed(nums[i + 1:])