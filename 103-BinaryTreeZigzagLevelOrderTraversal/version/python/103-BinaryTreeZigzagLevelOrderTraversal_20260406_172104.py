# Last updated: 4/6/2026, 5:21:04 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root: return []
10        
11        q = deque([root])
12        zigZag = []
13        direction = 1
14
15        while q:
16            level = []
17            for _ in range(len(q)):
18                curr = q.popleft()
19                level.append(curr.val)
20
21                if curr.left: q.append(curr.left)
22                if curr.right: q.append(curr.right)
23
24            zigZag.append(level[::direction])
25            direction = -direction
26        
27        return zigZag
28
29
30
31
32
33
34        
35        