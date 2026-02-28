# Last updated: 2/28/2026, 4:27:29 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashSet = set()
        ans = set()

        for num in nums1:
            hashSet.add(num)

        for num in nums2:
            if num in hashSet:
                ans.add(num)
        
        return list(ans)
