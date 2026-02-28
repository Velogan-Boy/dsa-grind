# Last updated: 2/28/2026, 4:27:54 PM
class Solution(object):
    def containsDuplicate(self, nums):
        
        numSet = set(nums)

        if len(numSet) != len(nums): return True
        else: return False
        