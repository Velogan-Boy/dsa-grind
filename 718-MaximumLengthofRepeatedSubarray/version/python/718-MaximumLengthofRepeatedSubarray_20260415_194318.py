# Last updated: 4/15/2026, 7:43:18 PM
1class Solution:
2    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
3        n = len(nums1)
4        m = len(nums2)
5        
6        prev = [0] * (m + 1)
7
8        ans = 0
9        for i in range(1, n + 1):
10            curr = [0] * (n + 1)
11            for j in range(1, m + 1):
12                if nums1[i - 1] == nums2[j - 1]:
13                    curr[j] = 1 + prev[j - 1]
14                    ans = max(ans, curr[j])
15                else:
16                    curr[j] = 0
17
18            prev = curr
19        
20        return ans
21        