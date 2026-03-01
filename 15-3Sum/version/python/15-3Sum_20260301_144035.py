# Last updated: 3/1/2026, 2:40:35 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        nums.sort()
5
6        for i, a in enumerate(nums):
7            if i > 0 and nums[i - 1] == a: continue
8
9            if a > 0: break
10
11            left = i + 1
12            right = len(nums) - 1
13
14            while left < right:
15                currSum = a + nums[left] + nums[right]
16
17                if currSum < 0: left+=1
18                elif currSum > 0: right-=1
19                else:
20                    res.append([a,nums[left],nums[right]])
21                    left +=1
22                    right -= 1
23                    while nums[left] == nums[left - 1] and left < right: left += 1
24                    while nums[right] == nums[right + 1] and left < right: right -= 1 
25
26        return res
27                
28
29
30
31
32
33
34
35
36
37
38        
39