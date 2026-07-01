# Last updated: 7/1/2026, 10:59:32 PM
1class Solution:
2    def nextGreaterElements(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        nge = [-1] * n
5        stack = []
6
7        for i in range(n*2-1, -1, -1):
8            while stack and stack[-1] <= nums[i % n]:
9                stack.pop()
10            
11            if i < n:
12                nge[i] = stack[-1] if stack else -1
13            
14            stack.append(nums[i % n])
15
16        return nge
17
18        
19
20        