# Last updated: 7/12/2026, 6:17:10 PM
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        nums.sort()

        for card in nums:
            if count[card] == 0:
                continue

            for i in range(k):
                if count[card + i] == 0:
                    return False
                count[card + i] -= 1

        return True
        