# Last updated: 4/8/2026, 11:46:05 PM
1class Solution:
2    def lowestCommonAncestor(self, root, p, q):
3        ans = None
4
5        def traverse(node):
6            nonlocal ans
7            if not node:
8                return False
9
10            left = traverse(node.left)
11            right = traverse(node.right)
12
13            mid = (node == p or node == q)
14
15            if mid + left + right >= 2:
16                ans = node
17
18            return mid or left or right
19
20        traverse(root)
21        return ans