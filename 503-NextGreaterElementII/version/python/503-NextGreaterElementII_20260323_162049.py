# Last updated: 3/23/2026, 4:20:49 PM
1class Solution:
2    def nextGreaterElements(self, nums: List[int]) -> List[int]:
3
4        n = len(nums)
5        stack = []
6        ans = [-1] * n
7
8        for i in range(2*n-1, -1, -1):
9            while stack and stack[-1] <= nums[i % n]:
10                stack.pop()
11            
12            if i < n:
13                ans[i] = stack[-1] if stack else -1
14            
15            stack.append(nums[i % n])
16
17        return ans
18
19        
20
21        