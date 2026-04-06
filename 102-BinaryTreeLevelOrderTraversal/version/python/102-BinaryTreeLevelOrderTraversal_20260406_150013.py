# Last updated: 4/6/2026, 3:00:13 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9            ans = []
10
11            if not root: return ans
12
13            queue = []
14
15            queue.append(root)
16
17            while queue:
18                level = []
19
20                for _i in range(len(queue)):
21                    node = queue.pop(0)
22                    level.append(node.val)
23
24                    if node.left: queue.append(node.left)
25                    if node.right: queue.append(node.right)
26                
27                ans.append(level)
28
29            
30
31            return ans
32            
33
34
35
36
37
38
39
40
41
42
43        