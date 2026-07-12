# Last updated: 7/12/2026, 6:16:09 PM
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i , j = 0, 0
        count = 0
        n = len(nums)

        while i < n and j < n:
            while i < n and nums[i] != 0 and i < n: i += 1
            j = i + 1

            if i >= n: break

            while j < n and nums[j] == 0: j += 1

            l = j - i

            count += l * (l + 1) // 2

            i = j + 1

        return count








        