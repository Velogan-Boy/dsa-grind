# Last updated: 7/12/2026, 6:18:01 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def reqHours(k):
            hoursTaken = 0
            for pile in piles:
                hoursTaken += ceil(pile/k)

            return hoursTaken
            

        while low <= high:
            k = (low + high) // 2

            if reqHours(k) <= h:
                high = k - 1
            else:
                low = k + 1
        
        return low






        