# Last updated: 3/22/2026, 2:19:04 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3
4        n = len(nums)
5        subsets = 1 << n
6        ans = []
7
8        for i in range(subsets):
9            list = []
10            for j in range(n):
11                if i & (1 << j):
12                    list.append(nums[j])
13
14            ans.append(list)
15
16        return ans
17
18
19            
20        