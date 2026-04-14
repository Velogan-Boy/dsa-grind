# Last updated: 4/14/2026, 1:29:50 PM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        totalSum = sum(nums)
4        if totalSum % 2 != 0: return False
5        n = len(nums)
6
7        target = totalSum // 2
8
9        prev = [False] * (target + 1) 
10        prev[0] = True
11
12        if nums[0] <= target:
13            prev[nums[0]] = True
14        
15        for i in range(1, n):
16            curr = [False] * (target + 1)
17            curr[0] = True
18
19            for j in range(1, target + 1):
20                notPick = prev[j]
21
22                pick = False
23                if nums[i] <= j:
24                    pick = prev[j - nums[i]]
25
26                curr[j] = pick or notPick
27            
28            prev = curr
29
30
31        return prev[target]
32