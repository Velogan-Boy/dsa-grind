# Last updated: 2/28/2026, 4:26:27 PM
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:

        nums.sort()

        minDiff = nums[-1] - nums[0]

        n = len(nums)

        for i in range(n - 1):
            high = max(nums[-1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i + 1] - k)

            minDiff = min(minDiff, high - low)

        return minDiff


        