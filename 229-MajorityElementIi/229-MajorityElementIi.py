# Last updated: 2/27/2026, 5:19:28 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # 1st pass: find up to two candidates
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # 2nd pass: verify the candidates
        result = []
        for c in [candidate1, candidate2]:
            if c is not None and nums.count(c) > len(nums) // 3:
                result.append(c)
        return result