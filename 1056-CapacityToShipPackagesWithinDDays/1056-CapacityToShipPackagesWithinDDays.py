# Last updated: 7/12/2026, 6:17:31 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = max(weights)
        e = sum(weights)
        
        while s <= e:
            capacity = (s + e) // 2

            actualDays = 0
            totalWeight = 0
            for weight in weights:
                if totalWeight + weight > capacity:
                    actualDays+=1
                    totalWeight = weight
                else:
                    totalWeight += weight
            
            if totalWeight != 0: actualDays+=1

            if actualDays <= days: 
                e = capacity - 1
            else:
                s = capacity + 1

        return s


