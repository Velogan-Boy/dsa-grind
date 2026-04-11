# Last updated: 4/11/2026, 8:29:19 PM
1class Solution:
2    def maxSumBST(self, root: Optional[TreeNode]) -> int:
3        ans = 0
4
5        def dfs(node):
6            nonlocal ans
7            if not node:
8                return inf, -inf, 0
9            
10            lmin,lmax,lsum = dfs(node.left)
11            rmin,rmax,rsum = dfs(node.right)
12
13            if lmax < node.val < rmin:
14                currSum = lsum + rsum + node.val
15                ans = max(ans, currSum)
16
17                return min(node.val, lmin), max(node.val, rmax), currSum
18
19            else:
20                return -inf, inf, 0
21        
22        dfs(root)
23
24        return ans
25
26            
27        