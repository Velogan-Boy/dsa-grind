# Last updated: 4/6/2026, 2:47:52 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        
10        if not root:
11            return []
12
13        stack, output = [root], []
14
15        while stack:
16            node = stack.pop()
17            output.append(node.val)
18   
19            if node.left:
20                stack.append(node.left)
21            if node.right:
22                stack.append(node.right)
23
24      
25        return output[::-1]
26        
27        