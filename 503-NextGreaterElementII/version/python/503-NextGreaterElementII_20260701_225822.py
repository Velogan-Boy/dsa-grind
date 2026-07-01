# Last updated: 7/1/2026, 10:58:22 PM
1class Solution:
2    def nextGreaterElements(self, nums: List[int]) -> List[int]:
3
4        n = len(nums)
5        nge = [-1] * n
6        stack = []
7
8        for i in range(n*2-1, -1, -1):
9            while stack and stack[-1] <= nums[i % n]:
10                stack.pop()
11            
12            if i < n:
13                nge[i] = stack[-1] if stack else -1
14            
15            stack.append(nums[i % n])
16
17        return nge
18
19        
20
21        