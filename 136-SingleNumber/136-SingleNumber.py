# Last updated: 2/27/2026, 5:22:14 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ans = 0

        for num in nums:
            ans ^= num

        return ans
        