# Last updated: 3/18/2026, 3:09:18 PM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        ans = []
4        def helper(i, currSum, curr):
5            if currSum == 0:
6                ans.append(curr[:])
7                return
8
9            if currSum < 0 or i == len(candidates):
10                return
11            
12            curr.append(candidates[i])
13            helper(i + 1, currSum - candidates[i], curr)
14
15            curr.pop()
16            for ind in range(i + 1, len(candidates)):
17                if candidates[ind] != candidates[i]:
18                    helper(ind, currSum, curr)
19                    break
20
21
22        candidates.sort()
23        helper(0, target, [])
24
25        return ans