# Last updated: 3/1/2026, 3:46:18 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        n = len(nums)
5
6        ans = set()
7
8        for i in range(n):
9            if i != 0 and nums[i - 1] == nums[i]: continue
10
11            for j in range(i+1, n):
12                if j != i + 1 and  nums[j - 1] == nums[j]: continue
13
14                l = j + 1
15                k = n - 1
16
17                while l < k:
18                    quadSum = nums[i] + nums[j] + nums[k] + nums[l]
19
20                    if quadSum < target:
21                        l+=1
22                    elif quadSum > target:
23                        k-=1
24                    else:
25                        ans.add((nums[i],nums[j],nums[l],nums[k]))
26
27                        l+=1
28                        k-=1
29
30                        while l < k and nums[l - 1] == nums[l]: l+=1
31                        while l < k and nums[k] == nums[k + 1]: k-=1
32
33
34        return list(ans)
35
36
37
38
39        