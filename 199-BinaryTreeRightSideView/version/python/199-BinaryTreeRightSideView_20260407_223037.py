# Last updated: 4/7/2026, 10:30:37 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        if not root: return []
10
11        q = deque([root])
12        ans = []
13
14        while q:
15            size = len(q)
16            for i in range(size):
17                curr = q.popleft()
18
19                if curr.left: q.append(curr.left)
20                if curr.right: q.append(curr.right)
21
22                if i == size - 1:
23                    ans.append(curr.val)
24        return ans
25                
26
27
28
29
30
31
32
33        