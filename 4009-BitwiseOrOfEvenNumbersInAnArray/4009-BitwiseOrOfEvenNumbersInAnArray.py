# Last updated: 2/28/2026, 4:25:40 PM
class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:

        ans = 0
        for num in nums:
            if num % 2 == 0: ans |= num

        return ans