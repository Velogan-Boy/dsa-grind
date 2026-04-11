# Last updated: 4/11/2026, 3:35:58 PM
1class Solution:
2    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
3        i = 1
4        ans = -1
5
6        def inorderTraverse(node):
7            nonlocal ans
8            nonlocal i
9
10            if not node: return
11
12            inorderTraverse(node.left)
13            if i == k: ans = node.val
14            i+=1
15            inorderTraverse(node.right)
16        
17        inorderTraverse(root)
18        return ans