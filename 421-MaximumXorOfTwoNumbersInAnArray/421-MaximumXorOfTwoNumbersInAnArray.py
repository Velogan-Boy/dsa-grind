# Last updated: 7/12/2026, 6:19:46 PM
class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0
        
        for i in range(31, -1, -1):
            mask |= (1 << i)
            
            prefixes = set()
            
            for num in nums:
                prefixes.add(num & mask)
            
            candidate = max_xor | (1 << i)
            
            for prefix in prefixes:
                if (prefix ^ candidate) in prefixes:
                    max_xor = candidate
                    break
        
        return max_xor


