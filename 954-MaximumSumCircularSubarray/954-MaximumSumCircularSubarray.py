# Last updated: 7/12/2026, 6:17:57 PM
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        currMax = globalMax = nums[0]
        currMin = globalMin = nums[0]

        for num in nums[1:]:
            currMax = max(num, currMax + num)
            globalMax = max(globalMax, currMax)

            currMin = min(num, currMin + num)
            globalMin = min(globalMin, currMin)

        if globalMax < 0:
            return globalMax

        return max(globalMax, total - globalMin)