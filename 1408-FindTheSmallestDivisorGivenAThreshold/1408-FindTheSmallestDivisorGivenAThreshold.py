# Last updated: 7/12/2026, 6:17:12 PM
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if threshold == 0:
            return 1

        s = 1
        e = max(nums)

        while s <= e:
            x = (s + e) // 2

            sumOfResult = 0
            for num in nums:
                sumOfResult += math.ceil(num / x)

            if sumOfResult <= threshold:
                e = x - 1
            else:
                s = x + 1

        return s