# Last updated: 7/12/2026, 6:18:38 PM
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        
        prev = [0] * (m + 1)

        ans = 0
        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                    ans = max(ans, curr[j])
                else:
                    curr[j] = 0

            prev = curr
        
        return ans
        