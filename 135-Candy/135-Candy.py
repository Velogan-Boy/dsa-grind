# Last updated: 7/12/2026, 6:22:27 PM
class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)

        left = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        
        right = 1
        ans = max(1, left[n-1])
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                curr = right + 1
            else:
                curr = 1
            
            right = curr
            
            ans += max(curr, left[i])

        return ans




        