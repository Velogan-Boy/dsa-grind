# Last updated: 2/27/2026, 10:35:07 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixSum = 0
        prefixMap = {0: 1}
        count = 0

        for num in nums:
            prefixSum += num

            x = prefixSum - k
            if x in prefixMap:
                count += prefixMap[x]

            prefixMap[prefixSum] = prefixMap.get(prefixSum, 0) + 1

        return count