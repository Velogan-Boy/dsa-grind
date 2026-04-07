# Last updated: 4/7/2026, 10:20:21 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8     def verticalTraversal(self, root):
9
10        if not root:
11            return []
12
13        nodes_map = defaultdict(lambda: defaultdict(list))
14
15        queue = deque([(root, 0, 0)])  
16
17        while queue:
18            node, x, y = queue.popleft()
19
20            nodes_map[x][y].append(node.val)
21
22            if node.left:
23                queue.append((node.left, x - 1, y + 1))
24
25            if node.right:
26                queue.append((node.right, x + 1, y + 1))
27
28        result = []
29        for x in sorted(nodes_map):
30            column = []
31            for y in sorted(nodes_map[x]):
32                column.extend(sorted(nodes_map[x][y]))
33            result.append(column)
34
35        return result
36
37        