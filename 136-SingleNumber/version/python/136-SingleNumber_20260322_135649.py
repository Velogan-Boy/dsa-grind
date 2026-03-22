# Last updated: 3/22/2026, 1:56:49 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        
4        ans = 0
5        for num in nums:
6            ans ^= num
7
8        return ans
9
10        