# Last updated: 7/12/2026, 6:16:22 PM
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * n

        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        
        runningSum = 0
        ans = -1
        for i in range(n - 1, -1, -1):
            if runningSum == prefixSum[i]:
                ans = i
            
            runningSum += nums[i]
        
        return ans



        