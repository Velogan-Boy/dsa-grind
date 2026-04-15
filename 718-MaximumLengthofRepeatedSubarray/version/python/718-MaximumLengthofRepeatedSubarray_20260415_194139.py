# Last updated: 4/15/2026, 7:41:39 PM
1class Solution:
2    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
3        n = len(nums1)
4        m = len(nums2)
5        
6        dp = [[0] * (m + 1) for _ in range(n + 1)]
7
8        ans = 0
9        for i in range(1, n + 1):
10            for j in range(1, m + 1):
11                if nums1[i - 1] == nums2[j - 1]:
12                    dp[i][j] = 1 + dp[i - 1][j - 1]
13                    ans = max(ans, dp[i][j])
14                else:
15                    dp[i][j] = 0
16        
17        return ans
18        