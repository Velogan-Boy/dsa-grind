# Last updated: 4/6/2026, 2:35:36 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        ans = []
10        if not root: return ans
11
12        stack = [root]
13
14        while stack:
15            node = stack.pop()
16
17            ans.append(node.val)
18
19            if node.right: stack.append(node.right)
20            if node.left: stack.append(node.left)
21        
22
23        return ans
24        