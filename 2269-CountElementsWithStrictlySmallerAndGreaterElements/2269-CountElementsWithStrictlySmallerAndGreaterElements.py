# Last updated: 2/28/2026, 4:25:45 PM
class Solution:
    def countElements(self, nums: List[int]) -> int:

        minElement = inf
        maxElement = -inf

        for x in nums:
            minElement = min(x, minElement)
            maxElement = max(x, maxElement)

        count = 0
        for x in nums:
            if x > minElement and x < maxElement:
                count+=1
        

        return count
        