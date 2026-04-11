# Last updated: 4/11/2026, 3:00:50 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9
10        if not root: return TreeNode(val)
11
12        curr = root
13
14        while curr:
15            if curr.val < val:
16                if not curr.right:
17                    curr.right = TreeNode(val)
18                    break
19
20                curr = curr.right
21            else:
22                if not curr.left:
23                    curr.left = TreeNode(val)
24                    break
25
26                curr = curr.left
27            
28        return root
29
30
31        