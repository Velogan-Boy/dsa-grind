# Last updated: 6/4/2026, 12:27:29 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9
10        if not root: return []
11
12        q = deque([root])
13        ans = []
14
15        while q:
16            size = len(q)
17
18            level = []
19            for _ in range(size):
20                node = q.popleft()
21                level.append(node.val)
22
23                if node.left: q.append(node.left)
24                if node.right: q.append(node.right)
25
26            ans.append(level)
27                
28
29        return ans
30
31
32        