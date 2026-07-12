# Last updated: 7/12/2026, 6:16:52 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        nums.sort()

        return (nums[-1] - 1) * (nums[-2] - 1)
        