# Last updated: 2/27/2026, 5:23:58 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxiSum = -inf
        currSum = 0

        for num in nums:
            currSum += num

            if currSum > maxiSum:
                maxiSum = currSum

            if currSum < 0:
                currSum = 0
            

        return maxiSum
        