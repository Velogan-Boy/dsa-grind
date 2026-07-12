# Last updated: 7/12/2026, 6:19:27 PM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n
        stack = []

        for i in range(n*2-1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            
            if i < n:
                nge[i] = stack[-1] if stack else -1
            
            stack.append(nums[i % n])

        return nge

        

        