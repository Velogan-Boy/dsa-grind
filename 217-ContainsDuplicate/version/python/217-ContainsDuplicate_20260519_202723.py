# Last updated: 5/19/2026, 8:27:23 PM
1class Solution(object):
2    def containsDuplicate(self, nums):
3        
4        numSet = set(nums)
5
6        if len(numSet) != len(nums): return True
7        else: return False
8        