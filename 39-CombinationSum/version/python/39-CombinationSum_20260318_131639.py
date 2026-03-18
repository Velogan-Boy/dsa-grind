# Last updated: 3/18/2026, 1:16:39 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3
4        ans = []
5        def helper(i, currSum, curr):
6            if currSum < 0 or i == len(candidates):
7                return
8            
9            if currSum == 0:
10                ans.append(curr[:])
11                return
12            
13            curr.append(candidates[i])
14            helper(i, currSum - candidates[i], curr)
15
16            curr.pop()
17            helper(i + 1, currSum, curr)
18
19
20        helper(0, target, [])
21
22        return ans
23
24
25
26        